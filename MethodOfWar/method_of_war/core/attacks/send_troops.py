from typing import List

from method_of_war.core.units.unit_models.a_unit import Unit
from method_of_war.ui.gameplay_ui.map.send_troops_table_list_view import SendTroopsElement
from method_of_war.ui.persistent_ui.troop_movements_view import TroopMovementElement
from method_of_war.ui.ui_global import *
from method_of_war.enums.attack_size import AttackSize
from mini_engine.util.vector2 import Vector2
from method_of_war.ui import ui_global
from method_of_war.core.attacks import global_battles


class SendTroops:
    __fromSettlement = None
    __toSettlement = None
    __currentUnitsToBeSentDict: dict
    __maxUnitsDict: dict
    _elementList: List[SendTroopsElement] = []
    _targetString: str
    _targetOwnerName: str
    __bigAttackThreshold: int = 10
    __smallAttackThreshold: int = 5

    def __init__(self, fromSettlement, toSettlement):
        self._elementList = []
        self.__fromSettlement = fromSettlement
        self.__toSettlement = toSettlement
        self.__setupCurrentUnits()
        self._targetOwnerName = toSettlement.getOwnerName()
        self._targetString = "(" + str(toSettlement.getLocation()[0]) + ", " + str(toSettlement.getLocation()[1]) + ")"
        self._setupElementList()

    def __setupCurrentUnits(self):
        self.__currentUnitsToBeSentDict = dict(self.__fromSettlement.getStationingUnitsDict())
        self.__maxUnitsDict = dict(self.__currentUnitsToBeSentDict)
        keysList = list(self.__currentUnitsToBeSentDict.keys())
        for key in keysList:
            self.__currentUnitsToBeSentDict[key] = 0

    def _setupElementList(self):
        self._elementList = []
        keysList = list(self.__currentUnitsToBeSentDict.keys())
        for key in keysList:
            self._setupElement(key)

    def _setupElement(self, key: str):
        self._elementList.append(SendTroopsElement(unitColorDict[key],
                                                   self.__maxUnitsDict[key],
                                                   self.__currentUnitsToBeSentDict[key],
                                                   lambda: self.addCurrentUnit(key, 1),
                                                   lambda: self.addCurrentUnit(key, 5),
                                                   lambda: self.__removeCurrentUnit(key, 1),
                                                   lambda: self.__removeCurrentUnit(key, 5),
                                                   lambda: self.__addAllToCurrentUnit(key),
                                                   lambda: self.__resetCurrentUnit(key)))

    def addCurrentUnit(self, name: str, quantity: int):
        self.__currentUnitsToBeSentDict[name] += quantity
        if self.__currentUnitsToBeSentDict[name] > self.__maxUnitsDict[name]:
            self.__currentUnitsToBeSentDict[name] = self.__maxUnitsDict[name]
        self._setupElementList()
        # print(self.__currentUnitsToBeSentDict)

    def __removeCurrentUnit(self, name: str, quantity: int):
        self.__currentUnitsToBeSentDict[name] -= quantity
        if self.__currentUnitsToBeSentDict[name] < 0:
            self.__currentUnitsToBeSentDict[name] = 0
        self._setupElementList()

    def __addAllToCurrentUnit(self, name: str):
        self.__currentUnitsToBeSentDict[name] = self.__maxUnitsDict[name]
        self._setupElementList()

    def __resetCurrentUnit(self, name: str):
        self.__currentUnitsToBeSentDict[name] = 0
        self._setupElementList()

    def _resetAll(self):
        keysList = list(self.__currentUnitsToBeSentDict.keys())
        for key in keysList:
            self.__currentUnitsToBeSentDict[key] = 0
        self._setupElementList()

    # TO-DO
    def sendAttack(self):
        # add new element to troop movements

        # determine attack size
        unitsCount: int = 0
        keysList = list(self.__currentUnitsToBeSentDict.keys())
        for key in keysList:
            unitsCount += self.__currentUnitsToBeSentDict[key]
        attackSize: AttackSize
        if unitsCount > self.__bigAttackThreshold:
            attackSize = AttackSize.BIG
        elif unitsCount < self.__smallAttackThreshold:
            attackSize = AttackSize.SMALL
        else:
            attackSize = AttackSize.MIDSIZED

        # determine if attacks come from an enemy
        fromEnemy = self._targetOwnerName == "Player"

        # determine movement speed of attacking army
        minMovementSpeed: float = 999
        for key in keysList:
            if self.__currentUnitsToBeSentDict[key] > 0:
                tempUnit: Unit = self.__fromSettlement.findStationingUnitInListByName(key)
                if tempUnit.getMovementSpeed() < minMovementSpeed:
                    minMovementSpeed = tempUnit.getMovementSpeed()

        # calculate time to battle
        fromVector: Vector2 = Vector2(self.__fromSettlement.getLocation()[0], self.__fromSettlement.getLocation()[1])
        toVector: Vector2 = Vector2(self.__toSettlement.getLocation()[0], self.__toSettlement.getLocation()[1])
        distanceBetweenSettlements = fromVector.distanceFrom(toVector)
        timeToBattle: float = distanceBetweenSettlements / minMovementSpeed

        troopMovementElement = TroopMovementElement(
            attackSize=attackSize,
            fromEnemy=fromEnemy,
            attackingSettlement=self.__fromSettlement.getOwnerName() + " " + self.__fromSettlement.getLocationStr(),
            defendingSettlement=self.__toSettlement.getOwnerName() + " " + self.__toSettlement.getLocationStr(),
            secondsToBattle=int(timeToBattle),
            realTimeToFinish=timeToBattle,
            attackingArmy=self.__currentUnitsToBeSentDict,
            defendingArmy=self.__toSettlement.getStationingUnitsDict(),
            attackingPlayer=self.__fromSettlement.getOwnerName(),
            defendingPlayer=self.__toSettlement.getOwnerName(),
            attackingSettlementLocation=self.__fromSettlement.getLocation(),
            defendingSettlementLocation=self.__toSettlement.getLocation(),
            elemId=global_battles.troopMovementIdIter
        )
        self.__fromSettlement.getTroopMovements().addElementToQueue(troopMovementElement)
        self.__toSettlement.getTroopMovements().addElementToQueue(troopMovementElement.getCopy())
        global_battles.troopMovementIdIter += 1

        for key in keysList:
            self.__fromSettlement.removeStationingUnit(key, self.__currentUnitsToBeSentDict[key])
        self.__setupCurrentUnits()
        self._setupElementList()
        # print("Just sent an attack.")

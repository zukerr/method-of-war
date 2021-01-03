from typing import List
from method_of_war.ui.gameplay_ui.map.send_troops_table_list_view import SendTroopsElement
from method_of_war.ui.ui_global import *


class SendTroops:
    __settlement = None
    __currentUnitsToBeSentDict: dict
    __maxUnitsDict: dict
    _elementList: List[SendTroopsElement] = []
    _targetString: str
    _ownerName: str

    def __init__(self, fromSettlement, toSettlement):
        self._elementList = []
        self.__settlement = fromSettlement
        self.__setupCurrentUnits()
        self._ownerName = toSettlement.getOwnerName()
        self._targetString = "(" + str(toSettlement.getLocation()[0]) + ", " + str(toSettlement.getLocation()[1]) + ")"
        self._setupElementList()

    def __setupCurrentUnits(self):
        self.__currentUnitsToBeSentDict = dict(self.__settlement.getStationingUnitsDict())
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
                                                   lambda: self.__addCurrentUnit(key, 1),
                                                   lambda: self.__addCurrentUnit(key, 5),
                                                   lambda: self.__removeCurrentUnit(key, 1),
                                                   lambda: self.__removeCurrentUnit(key, 5),
                                                   lambda: self.__addAllToCurrentUnit(key),
                                                   lambda: self.__resetCurrentUnit(key)))

    def __addCurrentUnit(self, name: str, quantity: int):
        self.__currentUnitsToBeSentDict[name] += quantity
        if self.__currentUnitsToBeSentDict[name] > self.__maxUnitsDict[name]:
            self.__currentUnitsToBeSentDict[name] = self.__maxUnitsDict[name]
        self._setupElementList()
        print(self.__currentUnitsToBeSentDict)

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
            self.__resetCurrentUnit(key)
        self._setupElementList()

    # TO-DO
    def _sendAttack(self):
        # add new element to troop movements
        # self.__settlement....
        print("Just sent an attack.")
        pass

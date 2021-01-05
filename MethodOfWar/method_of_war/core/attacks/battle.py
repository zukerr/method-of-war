from method_of_war.enums.battle_result import BattleResult
from method_of_war.ui.persistent_ui.troop_movements_view import TroopMovementElement
from method_of_war.core.units.unit_models.unit_factory import MakeUnit
from method_of_war.core.units.unit_models.a_unit import *
from typing import List
from typing import Optional
import random
from method_of_war.core.attacks import global_battles


class Battle:
    __troopMovementElement: TroopMovementElement
    __initialRangedExchangeIterations: int = 3

    __initialAttackingArmy: dict
    __initialDefendingArmy: dict
    __attackingLosses: dict
    __defendingLosses: dict

    def __init__(self, troopMovementElement: TroopMovementElement):
        self.__troopMovementElement = troopMovementElement
        if global_battles.globalBattleId != self.__troopMovementElement.elemId:
            self.__calculateBattle(self.__troopMovementElement.attackingArmy, self.__troopMovementElement.defendingArmy)
            global_battles.globalBattleId = self.__troopMovementElement.elemId
            global_battles.globalBattleList.append(self)
        else:
            correspondingBattle = global_battles.globalBattleList[len(global_battles.globalBattleList) - 1]
            self.__troopMovementElement = correspondingBattle.__troopMovementElement
            self.__initialAttackingArmy = correspondingBattle.__initialAttackingArmy
            self.__initialDefendingArmy = correspondingBattle.__initialDefendingArmy
            self.__attackingLosses = correspondingBattle.__attackingLosses
            self.__defendingLosses = correspondingBattle.__defendingLosses

    def __calculateBattle(self, attackingArmy: dict, defendingArmy: dict):
        self.__initialAttackingArmy = dict(attackingArmy)
        self.__initialDefendingArmy = dict(defendingArmy)
        attackingArmyUnitList = self.__getListOfUnitsFromDict(attackingArmy)
        defendingArmyUnitList = self.__getListOfUnitsFromDict(defendingArmy)

        # ranged exchange
        rangedAttackers = self.__getAllRangedFromUnitList(attackingArmyUnitList)
        rangedDefenders = self.__getAllRangedFromUnitList(defendingArmyUnitList)
        for i in range(self.__initialRangedExchangeIterations):
            for ranged in rangedAttackers:
                target: Unit = self.__getRandomListElement(defendingArmyUnitList)
                ranged.dealDamageToOther(target)
                if target.getIsDead():
                    defendingArmyUnitList.remove(target)
            for ranged in rangedDefenders:
                target = self.__getRandomListElement(attackingArmyUnitList)
                ranged.dealDamageToOther(target)
                if target.getIsDead():
                    attackingArmyUnitList.remove(target)

        # full blown combat
        while (len(attackingArmyUnitList) > 0) and (len(defendingArmyUnitList) > 0):
            # print("Attacking units:")
            # print(len(attackingArmyUnitList))
            # print("Defending units:")
            # print(len(defendingArmyUnitList))

            rangedAttackers = self.__getAllRangedFromUnitList(attackingArmyUnitList)
            rangedDefenders = self.__getAllRangedFromUnitList(defendingArmyUnitList)
            meleeAttackers = self.__getAllMeleeFromUnitList(attackingArmyUnitList)
            meleeDefenders = self.__getAllMeleeFromUnitList(defendingArmyUnitList)

            self.__meleeDamageExchange(meleeAttackers,
                                       meleeDefenders,
                                       rangedDefenders,
                                       attackingArmyUnitList,
                                       defendingArmyUnitList)

            rangedAttackers = self.__getAllRangedFromUnitList(attackingArmyUnitList)
            rangedDefenders = self.__getAllRangedFromUnitList(defendingArmyUnitList)
            meleeAttackers = self.__getAllMeleeFromUnitList(attackingArmyUnitList)
            meleeDefenders = self.__getAllMeleeFromUnitList(defendingArmyUnitList)

            self.__meleeDamageExchange(meleeDefenders,
                                       meleeAttackers,
                                       rangedAttackers,
                                       defendingArmyUnitList,
                                       attackingArmyUnitList)

            for ranged in rangedAttackers:
                if len(defendingArmyUnitList) > 0:
                    target: Unit = self.__getRandomListElement(defendingArmyUnitList)
                    ranged.dealDamageToOther(target)
                    if target.getIsDead():
                        defendingArmyUnitList.remove(target)
            for ranged in rangedDefenders:
                if len(attackingArmyUnitList) > 0:
                    target = self.__getRandomListElement(attackingArmyUnitList)
                    ranged.dealDamageToOther(target)
                    if target.getIsDead():
                        attackingArmyUnitList.remove(target)

        # cleanup input dictionaries
        keyList = list(attackingArmy.keys())
        for key in keyList:
            attackingArmy[key] = len(self.__getAllUnitsWithNameFromList(attackingArmyUnitList, key))
            defendingArmy[key] = len(self.__getAllUnitsWithNameFromList(defendingArmyUnitList, key))

        # count losses
        self.__attackingLosses = self.__getArmyLosses(self.__initialAttackingArmy, attackingArmy)
        self.__defendingLosses = self.__getArmyLosses(self.__initialDefendingArmy, defendingArmy)

    def __meleeDamageExchange(self,
                              meleeAttackers: List[Unit],
                              meleeDefenders: List[Unit],
                              rangedDefenders: List[Unit],
                              attackingArmyUnitList: List[Unit],
                              defendingArmyUnitList: List[Unit]):
        meleeToRemove = []
        for melee in meleeAttackers:
            if not melee.getIsDead():
                target: Optional[Unit]
                if len(meleeDefenders) > 0:
                    target = self.__getRandomListElement(meleeDefenders)
                elif len(rangedDefenders) > 0:
                    target = self.__getRandomListElement(rangedDefenders)
                else:
                    target = None
                if target is not None:
                    melee.dealDamageToOther(target)
                    if target.getIsDead():
                        if target in defendingArmyUnitList:
                            defendingArmyUnitList.remove(target)
                        meleeDefenders = self.__getAllMeleeFromUnitList(defendingArmyUnitList)
                    else:
                        # counter attack
                        target.dealDamageToOther(melee)
                        if melee.getIsDead():
                            meleeToRemove.append(melee)
        for elem in meleeToRemove:
            attackingArmyUnitList.remove(elem)
            meleeAttackers = self.__getAllMeleeFromUnitList(attackingArmyUnitList)

    def __getListOfUnitsFromDict(self, army: dict) -> List[Unit]:
        resultList = []
        keyList = list(army.keys())
        for key in keyList:
            for i in range(army[key]):
                resultList.append(MakeUnit(key))
        return resultList

    def __getRandomMeleeFromUnitList(self, unitList: List[Unit]) -> Unit:
        return self.__getRandomListElement(self.__getAllMeleeFromUnitList(unitList))

    def __getAllMeleeFromUnitList(self, unitList: List[Unit]) -> List[Unit]:
        onlyMelee = []
        for unit in unitList:
            if unit.getIsMelee():
                onlyMelee.append(unit)
        return onlyMelee

    def __getAllRangedFromUnitList(self, unitList: List[Unit]) -> List[Unit]:
        only_ranged = []
        for unit in unitList:
            if not unit.getIsMelee():
                only_ranged.append(unit)
        return only_ranged

    def __getAllUnitsWithNameFromList(self, unitList: List[Unit], unitName: str) -> List[Unit]:
        filteredList = []
        for unit in unitList:
            if unit.getName() == unitName:
                filteredList.append(unit)
        return filteredList

    def __getRandomListElement(self, targetList: List):
        return targetList[random.randrange(len(targetList))]

    def attackingArmyWon(self) -> bool:
        keyList = list(self.__troopMovementElement.attackingArmy.keys())
        attackingUnitsCount: int = 0
        for key in keyList:
            attackingUnitsCount += self.__troopMovementElement.attackingArmy[key]
        if attackingUnitsCount > 0:
            return True
        else:
            return False

    def playerAttackedAndLost(self) -> bool:
        if not self.attackingArmyWon():
            if self.__troopMovementElement.attackingPlayer == "Player":
                return True
        return False

    def getBattleResult(self) -> BattleResult:
        keyList = list(self.__troopMovementElement.attackingArmy.keys())
        attackingUnitsCount: int = 0
        defendingUnitsCount: int = 0
        for key in keyList:
            attackingUnitsCount += self.__troopMovementElement.attackingArmy[key]
            defendingUnitsCount += self.__troopMovementElement.defendingArmy[key]
        if self.__troopMovementElement.attackingPlayer == "Player":
            if attackingUnitsCount > 0 >= defendingUnitsCount:
                return BattleResult.POSITIVE
            elif attackingUnitsCount <= 0 < defendingUnitsCount:
                return BattleResult.NEGATIVE
            else:
                return BattleResult.NEUTRAL
        else:
            if attackingUnitsCount > 0 >= defendingUnitsCount:
                return BattleResult.NEGATIVE
            elif attackingUnitsCount <= 0 < defendingUnitsCount:
                return BattleResult.POSITIVE
            else:
                return BattleResult.NEUTRAL

    def __getArmyLosses(self, armyBefore: dict, armyAfter: dict):
        resultDict = dict(armyBefore)
        keyList = list(resultDict.keys())
        for key in keyList:
            resultDict[key] = armyBefore[key] - armyAfter[key]
        return resultDict

    def getInitialAttackingArmy(self) -> dict:
        return self.__initialAttackingArmy

    def getInitialDefendingArmy(self) -> dict:
        return self.__initialDefendingArmy

    def getAttackingLosses(self) -> dict:
        return self.__attackingLosses

    def getDefendingLosses(self) -> dict:
        return self.__defendingLosses

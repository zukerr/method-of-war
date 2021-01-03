from method_of_war.ui.persistent_ui.troop_movements_view import TroopMovementElement
from method_of_war.core.units.unit_models.unit_factory import MakeUnit
from method_of_war.core.units.unit_models.a_unit import *
from typing import List
import random


class Battle:
    __troopMovementElement: TroopMovementElement
    __initialRangedExchangeIterations: int = 3

    def __init__(self, troopMovementElement: TroopMovementElement):
        self.__troopMovementElement = troopMovementElement
        self.__calculateBattle(self.__troopMovementElement.attackingArmy, self.__troopMovementElement.defendingArmy)

    def __calculateBattle(self, attackingArmy: dict, defendingArmy: dict):
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
            rangedAttackers = self.__getAllRangedFromUnitList(attackingArmyUnitList)
            rangedDefenders = self.__getAllRangedFromUnitList(defendingArmyUnitList)
            meleeAttackers = self.__getAllMeleeFromUnitList(attackingArmyUnitList)
            meleeDefenders = self.__getAllMeleeFromUnitList(defendingArmyUnitList)

            meleeToRemove = []
            for melee in meleeAttackers:
                if not melee.getIsDead():
                    target: Unit = self.__getRandomListElement(meleeDefenders)
                    melee.dealDamageToOther(target)
                    if target.getIsDead():
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

        # cleanup input dictionaries
        keyList = list(attackingArmy.keys())
        for key in keyList:
            attackingArmy[key] = len(self.__getAllUnitsWithNameFromList(attackingArmyUnitList, key))
            defendingArmy[key] = len(self.__getAllUnitsWithNameFromList(defendingArmyUnitList, key))

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
        return random.randrange(len(targetList))

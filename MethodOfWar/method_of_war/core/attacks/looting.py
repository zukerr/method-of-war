from method_of_war.core.units.unit_models.a_unit import Unit
from method_of_war.core.buildings.resources_requirement_model import ResourcesRequirementModel
from typing import List


class Looting:
    __lootedResourcesList: List[ResourcesRequirementModel] = []
    __lootedWood: int
    __lootedGranite: int
    __lootedIron: int
    __lootedSum: int
    __lootCapacity: int

    def __init__(self):
        self.__lootedResourcesList = []
        self.__lootedWood = 0
        self.__lootedGranite = 0
        self.__lootedIron = 0
        self.__lootedSum = 0
        self.__lootCapacity = 0

    def lootResources(self, lootingUnit: Unit, lootedSettlement):
        self.__lootedResourcesList.append(self.__lootResourcesAsSingleUnit(lootingUnit, lootedSettlement))

    def sumUpLooting(self):
        for reqModel in self.__lootedResourcesList:
            self.__lootedWood += reqModel.woodValue
            self.__lootedGranite += reqModel.graniteValue
            self.__lootedIron += reqModel.ironValue
        self.__lootedSum = self.__lootedWood + self.__lootedGranite + self.__lootedIron

    def __lootResourcesAsSingleUnit(self, lootingUnit: Unit, lootedSettlement) -> ResourcesRequirementModel:
        self.__lootCapacity += lootingUnit.getLootCapacity()
        # divide looting unit capacity to equal parts for each resource
        equalPart: int = int(lootingUnit.getLootCapacity() / 3)
        # get the rest that is present because of rounding down
        rest: int = lootingUnit.getLootCapacity() - (3 * equalPart)
        # count the bigger part
        biggerPart: int = equalPart + rest
        # now 2 equal parts and one bigger part should sum up to full loot capacity
        # check if we can just loot full capacity
        lootedWarehouse = lootedSettlement.getWarehouse()
        resourceRequirement = ResourcesRequirementModel(biggerPart, equalPart, equalPart, 0)
        if lootedWarehouse.requirementCanBeSatisfied(resourceRequirement):
            lootedWarehouse.spendRequirement(resourceRequirement)
            return resourceRequirement
        else:
            (settlementWood, settlementGranite, settlementIron) = lootedWarehouse.getCurrentResourceValues()
            onlyWoodReq = ResourcesRequirementModel(lootingUnit.getLootCapacity(), 0, 0, 0)
            if lootedWarehouse.requirementCanBeSatisfied(onlyWoodReq):
                lootedWarehouse.spendRequirement(onlyWoodReq)
                return onlyWoodReq
            else:
                leftToLoot = lootingUnit.getLootCapacity()
                woodToLoot = settlementWood
                leftToLoot -= woodToLoot
                if leftToLoot <= settlementGranite:
                    graniteToLoot = leftToLoot
                    woodAndGraniteReq = ResourcesRequirementModel(woodToLoot, graniteToLoot, 0, 0)
                    lootedWarehouse.spendRequirement(woodAndGraniteReq)
                    return woodAndGraniteReq
                else:
                    graniteToLoot = settlementGranite
                    leftToLoot -= graniteToLoot
                    if leftToLoot <= settlementIron:
                        ironToLoot = leftToLoot
                    else:
                        ironToLoot = settlementIron
                    fullReq = ResourcesRequirementModel(woodToLoot, graniteToLoot, ironToLoot, 0)
                    lootedWarehouse.spendRequirement(fullReq)
                    return fullReq

    def getLootedWood(self) -> int:
        return self.__lootedWood

    def getLootedGranite(self) -> int:
        return self.__lootedGranite

    def getLootedIron(self) -> int:
        return self.__lootedIron

    def getLootCapacity(self) -> int:
        return self.__lootCapacity

    def getLootedSum(self) -> int:
        return self.__lootedSum

from method_of_war.core.buildings.a_building import *
from method_of_war.ui import global_persistent_view_manager
from method_of_war.ui import global_gameplay_view_manager


class Warehouse(Building):
    __maxResourcesPerLevelDict = {
        1: 1000,
        2: 1294,
        3: 1502,
        4: 2105,
        5: 2632,
        6: 3512,
        7: 5321,
        8: 6092,
        9: 7213,
        10: 9591
    }

    __maxResources: float
    __currentWood: float
    __currentGranite: float
    __currentIron: float

    def __init__(self, startingLevel: int, startingWood: int, startingGranite: int, startingIron: int):
        super().__init__(startingLevel)
        self.__maxResources = self.__maxResourcesPerLevelDict[self._level]
        self.__currentWood = startingWood
        self.__currentGranite = startingGranite
        self.__currentIron = startingIron
        self.__syncTopActionBarView()
        self.__syncWarehouseBuildingView()

    def levelUp(self):
        super().levelUp()
        self.__maxResources = self.__maxResourcesPerLevelDict[self._level]
        self.__syncTopActionBarView()
        self.__syncWarehouseBuildingView()

    def setupMaxLvl(self):
        self._maxLevel = 10

    def setupName(self):
        self._name = "Warehouse"

    def setupUpgradeRequirements(self):
        for i in range(self._maxLevel):
            tempValue = i*i + (2*i) + 23
            self._upgradeRequirementsList.append(ResourcesRequirementModel(tempValue, tempValue, tempValue, i + 5))

    def gainWood(self, value: float):
        self.__currentWood += value
        if self.__currentWood > self.__maxResources:
            self.__currentWood = self.__maxResources
        self.__syncTopActionBarView()

    def gainGranite(self, value: float):
        self.__currentGranite += value
        if self.__currentGranite > self.__maxResources:
            self.__currentGranite = self.__maxResources
        self.__syncTopActionBarView()

    def gainIron(self, value: float):
        self.__currentIron += value
        if self.__currentIron > self.__maxResources:
            self.__currentIron = self.__maxResources
        self.__syncTopActionBarView()

    def spendWood(self, value: float):
        if self.__currentWood < value:
            return
        self.__currentWood -= value
        self.__syncTopActionBarView()

    def spendGranite(self, value: float):
        if self.__currentGranite < value:
            return
        self.__currentGranite -= value
        self.__syncTopActionBarView()

    def spendIron(self, value: float):
        if self.__currentIron < value:
            return
        self.__currentIron -= value
        self.__syncTopActionBarView()

    def requirementCanBeSatisfied(self, requirement: ResourcesRequirementModel) -> bool:
        if self.__currentWood >= requirement.woodValue:
            if self.__currentGranite >= requirement.graniteValue:
                if self.__currentIron >= requirement.ironValue:
                    return True
        return False

    def spendRequirement(self, requirement: ResourcesRequirementModel):
        self.spendWood(requirement.woodValue)
        self.spendGranite(requirement.graniteValue)
        self.spendIron(requirement.ironValue)

    def __syncTopActionBarView(self):
        global_persistent_view_manager.globalPersistentViewManager.getTopActionBar().updateWoodText(
            str(int(self.__currentWood)))
        global_persistent_view_manager.globalPersistentViewManager.getTopActionBar().updateGraniteText(
            str(int(self.__currentGranite)))
        global_persistent_view_manager.globalPersistentViewManager.getTopActionBar().updateIronText(
            str(int(self.__currentIron)))
        global_persistent_view_manager.globalPersistentViewManager.getTopActionBar().updateMaxResourcesText(
            str(int(self.__maxResources)))

    def __syncWarehouseBuildingView(self):
        global_gameplay_view_manager\
            .globalGameplayViewManager\
            .getOverview()\
            .getWarehouse()\
            .updateValues(self._level, int(self.__maxResources), self.__maxResourcesPerLevelDict[self._level + 1])

    def start(self):
        pass

    def update(self):
        pass

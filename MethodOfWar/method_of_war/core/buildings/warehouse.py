from method_of_war.core.buildings.a_building import *
from method_of_war.ui import global_persistent_view_manager
from method_of_war.ui import global_gameplay_view_manager


class Warehouse(Building):
    _maxResourcesPerLevelDict = {
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

    _maxResources: float
    _currentWood: float
    _currentGranite: float
    _currentIron: float

    def __init__(self, startingLevel: int, startingWood: int, startingGranite: int, startingIron: int):
        super().__init__(startingLevel)
        self._maxResources = self._maxResourcesPerLevelDict[self._level]
        self._currentWood = startingWood
        self._currentGranite = startingGranite
        self._currentIron = startingIron

    def levelUp(self):
        super().levelUp()
        self._maxResources = self._maxResourcesPerLevelDict[self._level]

    def setupMaxLvl(self):
        self._maxLevel = 10

    def setupName(self):
        self._name = "Warehouse"

    def setupUpgradeRequirements(self):
        for i in range(self._maxLevel):
            tempValue = i*i + (2*i) + 23
            self._upgradeRequirementsList.append(ResourcesRequirementModel(tempValue, tempValue, tempValue, i + 5))

    def gainWood(self, value: float):
        self._currentWood += value
        if self._currentWood > self._maxResources:
            self._currentWood = self._maxResources

    def gainGranite(self, value: float):
        self._currentGranite += value
        if self._currentGranite > self._maxResources:
            self._currentGranite = self._maxResources

    def gainIron(self, value: float):
        self._currentIron += value
        if self._currentIron > self._maxResources:
            self._currentIron = self._maxResources

    def spendWood(self, value: float):
        if self._currentWood < value:
            return
        self._currentWood -= value

    def spendGranite(self, value: float):
        if self._currentGranite < value:
            return
        self._currentGranite -= value

    def spendIron(self, value: float):
        if self._currentIron < value:
            return
        self._currentIron -= value

    def requirementCanBeSatisfied(self, requirement: ResourcesRequirementModel) -> bool:
        if self._currentWood >= requirement.woodValue:
            if self._currentGranite >= requirement.graniteValue:
                if self._currentIron >= requirement.ironValue:
                    return True
        return False

    def spendRequirement(self, requirement: ResourcesRequirementModel):
        self.spendWood(requirement.woodValue)
        self.spendGranite(requirement.graniteValue)
        self.spendIron(requirement.ironValue)

    def start(self):
        pass

    def update(self):
        pass

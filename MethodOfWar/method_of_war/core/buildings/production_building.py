from method_of_war.core.buildings.a_building import *
from method_of_war.ui import global_persistent_view_manager
from method_of_war.ui import global_gameplay_view_manager
from method_of_war.enums.resource_type import ResourceType
from method_of_war.core.buildings.warehouse import Warehouse


class ProductionBuilding(Building):
    _productionPerMinuteDict: dict = {
        1: 100,
        2: 121,
        3: 144,
        4: 169,
        5: 196,
        6: 225,
        7: 256,
        8: 289,
        9: 324,
        10: 361,
        11: 400,
        12: 441,
        13: 484,
        14: 529,
        15: 576,
        16: 625,
        17: 676,
        18: 729,
        19: 784,
        20: 841,
        21: 0
    }
    _currentProductionPerMinute: int
    _resourceType: ResourceType
    __warehouse: Warehouse

    __firstUpdate: bool = False
    __oldTime: float

    def __init__(self, startingLevel: int, resourceType: ResourceType, warehouse: Warehouse):
        super().__init__(startingLevel)
        self._resourceType = resourceType
        self.setupNameModded()
        self._currentProductionPerMinute = self._productionPerMinuteDict[self._level]
        self.__warehouse = warehouse

    def levelUp(self):
        super().levelUp()
        self._currentProductionPerMinute = self._productionPerMinuteDict[self._level]

    def setupUpgradeRequirements(self):
        for i in range(self._maxLevel):
            tempValue = i*i + i + 20
            self._upgradeRequirementsList.append(ResourcesRequirementModel(tempValue, tempValue, tempValue, i + 5))

    def setupMaxLvl(self):
        self._maxLevel = 20

    def setupName(self):
        pass

    def setupNameModded(self):
        if self._resourceType == ResourceType.WOOD:
            self._name = "Lumber Mill"
        elif self._resourceType == ResourceType.GRANITE:
            self._name = "Quarry"
        else:
            self._name = "Mine"

    def addAppropriateResourceToWarehouse(self, value: float):
        if self._resourceType == ResourceType.WOOD:
            self.__warehouse.gainWood(value)
        elif self._resourceType == ResourceType.GRANITE:
            self.__warehouse.gainGranite(value)
        else:
            self.__warehouse.gainIron(value)

    def start(self):
        pass

    def update(self):
        pass

    def updateOnRealTime(self, realTime: float):
        if not self.__firstUpdate:
            self.__firstUpdate = True
        else:
            producedValue: float = self._currentProductionPerMinute * ((realTime - self.__oldTime) / 60)
            self.addAppropriateResourceToWarehouse(producedValue)
        self.__oldTime = realTime

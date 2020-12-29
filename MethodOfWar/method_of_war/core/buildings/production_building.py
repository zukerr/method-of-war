from method_of_war.core.buildings.a_building import *
from method_of_war.ui import global_persistent_view_manager
from method_of_war.ui import global_gameplay_view_manager
from method_of_war.enums.resource_type import ResourceType
from method_of_war.core.buildings.warehouse import Warehouse


class ProductionBuilding(Building):
    __productionPerMinuteDict: dict = {
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
        20: 841
    }
    __currentProductionPerMinute: int
    __resourceType: ResourceType
    __warehouse: Warehouse

    __firstUpdate: bool = False
    __oldTime: float

    def __init__(self, startingLevel: int, resourceType: ResourceType, warehouse: Warehouse):
        super().__init__(startingLevel)
        self.__resourceType = resourceType
        self.setupNameModded()
        self.__currentProductionPerMinute = self.__productionPerMinuteDict[self._level]
        self.__warehouse = warehouse
        self.__updateAppropriateProductionViewSegment()

    def levelUp(self):
        super().levelUp()
        self.__currentProductionPerMinute = self.__productionPerMinuteDict[self._level]
        self.__updateAppropriateProductionViewSegment()

    def setupUpgradeRequirements(self):
        for i in range(self._maxLevel):
            tempValue = i*i + i + 50
            self._upgradeRequirementsList.append(ResourcesRequirementModel(tempValue, tempValue, tempValue, i + 5))

    def setupMaxLvl(self):
        self._maxLevel = 20

    def setupName(self):
        pass

    def setupNameModded(self):
        if self.__resourceType == ResourceType.WOOD:
            self._name = "Lumber Mill"
        elif self.__resourceType == ResourceType.GRANITE:
            self._name = "Quarry"
        else:
            self._name = "Mine"

    def __updateAppropriateProductionViewSegment(self):
        if self.__resourceType == ResourceType.WOOD:
            global_persistent_view_manager.globalPersistentViewManager.getProduction().updateProductionValues(woodValue=self.__currentProductionPerMinute)
            global_gameplay_view_manager\
                .globalGameplayViewManager\
                .getOverview()\
                .getLumberMill()\
                .updateValues(self._level,
                              self.__currentProductionPerMinute,
                              self.__productionPerMinuteDict[self._level + 1])
        elif self.__resourceType == ResourceType.GRANITE:
            global_persistent_view_manager.globalPersistentViewManager.getProduction().updateProductionValues(graniteValue=self.__currentProductionPerMinute)
            global_gameplay_view_manager \
                .globalGameplayViewManager \
                .getOverview() \
                .getQuarry() \
                .updateValues(self._level,
                              self.__currentProductionPerMinute,
                              self.__productionPerMinuteDict[self._level + 1])
        else:
            global_persistent_view_manager.globalPersistentViewManager.getProduction().updateProductionValues(ironValue=self.__currentProductionPerMinute)
            global_gameplay_view_manager \
                .globalGameplayViewManager \
                .getOverview() \
                .getMine() \
                .updateValues(self._level,
                              self.__currentProductionPerMinute,
                              self.__productionPerMinuteDict[self._level + 1])

    def addAppropriateResourceToWarehouse(self, value: float):
        if self.__resourceType == ResourceType.WOOD:
            self.__warehouse.gainWood(value)
        elif self.__resourceType == ResourceType.GRANITE:
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
            producedValue: float = self.__currentProductionPerMinute * ((realTime - self.__oldTime) / 60)
            self.addAppropriateResourceToWarehouse(producedValue)
        self.__oldTime = realTime

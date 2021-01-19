from method_of_war.core.buildings.production_building import *
from method_of_war.ui import global_persistent_view_manager, global_gameplay_view_manager


class PlayerProductionBuilding(ProductionBuilding):

    def __init__(self, startingLevel: int, resourceType: ResourceType, warehouse: Warehouse):
        super().__init__(startingLevel, resourceType, warehouse)
        self.__updateAppropriateProductionViewSegment()

    def levelUp(self):
        super().levelUp()
        self.__updateAppropriateProductionViewSegment()

    def __updateAppropriateProductionViewSegment(self):
        if self._resourceType == ResourceType.WOOD:
            global_persistent_view_manager.globalPersistentViewManager.getProduction().updateProductionValues(woodValue=self._currentProductionPerMinute)
            global_gameplay_view_manager\
                .globalGameplayViewManager\
                .getOverview()\
                .getLumberMill()\
                .updateValues(self._level,
                              self._currentProductionPerMinute,
                              self._productionPerMinuteDict[self._level + 1])
        elif self._resourceType == ResourceType.GRANITE:
            global_persistent_view_manager.globalPersistentViewManager.getProduction().updateProductionValues(graniteValue=self._currentProductionPerMinute)
            global_gameplay_view_manager \
                .globalGameplayViewManager \
                .getOverview() \
                .getQuarry() \
                .updateValues(self._level,
                              self._currentProductionPerMinute,
                              self._productionPerMinuteDict[self._level + 1])
        else:
            global_persistent_view_manager.globalPersistentViewManager.getProduction().updateProductionValues(ironValue=self._currentProductionPerMinute)
            global_gameplay_view_manager \
                .globalGameplayViewManager \
                .getOverview() \
                .getMine() \
                .updateValues(self._level,
                              self._currentProductionPerMinute,
                              self._productionPerMinuteDict[self._level + 1])

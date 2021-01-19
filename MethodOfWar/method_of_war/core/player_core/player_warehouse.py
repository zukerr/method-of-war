from method_of_war.core.buildings.warehouse import *
from method_of_war.ui import global_persistent_view_manager, global_gameplay_view_manager


class PlayerWarehouse(Warehouse):

    def __init__(self, startingLevel: int, startingWood: int, startingGranite: int, startingIron: int):
        super().__init__(startingLevel, startingWood, startingGranite, startingIron)
        self.__syncTopActionBarView()
        self.__syncWarehouseBuildingView()

    def levelUp(self):
        super().levelUp()
        self.__syncTopActionBarView()
        self.__syncWarehouseBuildingView()

    def gainWood(self, value: float):
        super().gainWood(value)
        self.__syncTopActionBarView()

    def gainGranite(self, value: float):
        super().gainGranite(value)
        self.__syncTopActionBarView()

    def gainIron(self, value: float):
        super().gainIron(value)
        self.__syncTopActionBarView()

    def spendWood(self, value: float):
        super().spendWood(value)
        self.__syncTopActionBarView()

    def spendGranite(self, value: float):
        super().spendGranite(value)
        self.__syncTopActionBarView()

    def spendIron(self, value: float):
        super().spendIron(value)
        self.__syncTopActionBarView()

    def __syncTopActionBarView(self):
        global_persistent_view_manager.globalPersistentViewManager.getTopActionBar().updateWoodText(
            str(int(self._currentWood)))
        global_persistent_view_manager.globalPersistentViewManager.getTopActionBar().updateGraniteText(
            str(int(self._currentGranite)))
        global_persistent_view_manager.globalPersistentViewManager.getTopActionBar().updateIronText(
            str(int(self._currentIron)))
        global_persistent_view_manager.globalPersistentViewManager.getTopActionBar().updateMaxResourcesText(
            str(int(self._maxResources)))

    def __syncWarehouseBuildingView(self):
        global_gameplay_view_manager\
            .globalGameplayViewManager\
            .getOverview()\
            .getWarehouse()\
            .updateValues(self._level, int(self._maxResources), self._maxResourcesPerLevelDict[self._level + 1])

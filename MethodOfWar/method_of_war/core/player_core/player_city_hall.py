from method_of_war.core.buildings.city_hall import *
from method_of_war.ui import global_gameplay_view_manager


class PlayerCityHall(CityHall):

    def levelUp(self):
        super().levelUp()
        self.__syncView()

    # queue
    def addUpgradeToQueue(self, building: Building):
        super().addUpgradeToQueue(building)
        # update ui
        global_gameplay_view_manager.globalGameplayViewManager.getOverview().getCityHall().updateQueue(self._buildingQueue)

    def _updateQueueContent(self, timePassed: float):
        super()._updateQueueContent(timePassed)
        global_gameplay_view_manager.globalGameplayViewManager.getOverview().getCityHall().updateQueue(
            self._buildingQueue)
        if global_gameplay_view_manager.globalGameplayViewManager.isCityHallViewActive():
            global_gameplay_view_manager.globalGameplayViewManager.getOverview().getCityHall().drawQueue()

    def _redrawAvailableBuildingsLive(self):
        if global_gameplay_view_manager.globalGameplayViewManager.isCityHallViewActive():
            global_gameplay_view_manager.globalGameplayViewManager.getOverview().getCityHall().disableView()
            global_gameplay_view_manager.globalGameplayViewManager.getOverview().getCityHall().drawView()

    # available buildings
    def setupAvailableBuildings(self):
        super().setupAvailableBuildings()
        self.__syncView()

    def __syncView(self):
        global_gameplay_view_manager.globalGameplayViewManager.getOverview().getCityHall().updateLevel(self._level)
        global_gameplay_view_manager.globalGameplayViewManager.getOverview().getCityHall().updateAvailableList(self._availableBuildingsList)

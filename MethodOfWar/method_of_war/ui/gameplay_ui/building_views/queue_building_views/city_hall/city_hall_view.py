from method_of_war.ui.gameplay_ui.building_views import building_header_view
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.city_hall.city_hall_queue_list_view import *
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.city_hall.city_hall_available_buildings_list_view import *
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.city_hall.city_hall_not_available_buildings_list_view import *
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.queue_building_view import QueueBuildingView
from typing import List


class CityHallView(QueueBuildingView):
    __notAvailableList: List[NotAvailableBuildingElement] = []

    __notAvailableBuildingsListView: CityHallNotAvailableBuildingsListView

    # it needs to take real city hall as init argument to set up
    def drawView(self):
        if self._availableListView is not None:
            self.disableView()
        print("drawing city hall view")
        # draw bg
        border_rect.draw(self._window, grey44, (0, 57, 997, 663))

        # draw building header view
        headerView = building_header_view.BuildingHeaderView(self._window, "City Hall", buildingColorDict["City Hall"],
                                                             "City Hall (Level " + str(self._level) + ")",
                                                             "In City Hall you can build new buildings"
                                                             " and upgrade existing ones. The higher level City Hall"
                                                             " has, the lower build times.")
        headerView.drawView()

        # draw queue list view
        self.drawQueue()

        # draw available buildings list view
        self.drawAvailable()

        # draw not available buildings list view
        self.__notAvailableBuildingsListView = \
            CityHallNotAvailableBuildingsListView(
                self._window, defaultY=(self._availableListView.getCurrentY()
                                        + self._availableListView.getElementHeight()))
        self.__notAvailableBuildingsListView.clearElements()
        for elem in self.__notAvailableList:
            self.__notAvailableBuildingsListView.addElement(elem, False)
        self.__notAvailableBuildingsListView.drawView()

    def _drawQueueSetup(self):
        # draw queue bg
        border_rect.draw(self._window, grey44, (0, 207, 997, 108))
        self._queueListView = CityHallQueueListView(self._window)

    def _drawAvailableSetup(self):
        self._availableListView = CityHallAvailableBuildingsListView(self._window)

    def updateNotAvailableList(self, notAvailableList: List[NotAvailableBuildingElement]):
        self.__notAvailableList = notAvailableList

from mini_engine.ui.a_view import *
from method_of_war.ui.ui_global import *
from mini_engine.ui import button
from method_of_war.ui.gameplay_ui.building_views import building_header_view
from method_of_war.ui.gameplay_ui.building_views.city_hall.city_hall_queue_list_view import *
from method_of_war.ui.gameplay_ui.building_views.city_hall.city_hall_available_buildings_list_view import *
from method_of_war.ui.gameplay_ui.building_views.city_hall.city_hall_not_available_buildings_list_view import *
from typing import List


class CityHallView(View):
    __level: int
    __queue: List[BuildingQueueElement] = []
    __availableList: List[AvailableBuildingElement] = []
    __notAvailableList: List[NotAvailableBuildingElement] = []

    __queueListView: CityHallQueueListView
    __availableBuildingsListView: CityHallAvailableBuildingsListView
    __notAvailableBuildingsListView: CityHallNotAvailableBuildingsListView

    # it needs to take real city hall as init argument to set up
    def drawView(self):
        # draw bg
        border_rect.draw(self._window, grey44, (0, 57, 997, 663))

        # draw building header view
        headerView = building_header_view.BuildingHeaderView(self._window, buildingColorDict["City Hall"],
                                                             "City Hall (Level " + str(self.__level) + ")",
                                                             "In City Hall you can build new buildings"
                                                             " and upgrade existing ones. The higher level City Hall"
                                                             " has, the lower build times.")
        headerView.drawView()

        # draw queue list view
        self.drawQueue()

        # draw available buildings list view
        self.__availableBuildingsListView = CityHallAvailableBuildingsListView(self._window)
        self.__availableBuildingsListView.clearElements()
        for elem in self.__availableList:
            self.__availableBuildingsListView.addElement(elem, False)
        self.__availableBuildingsListView.drawView()

        # draw not available buildings list view
        self.__notAvailableBuildingsListView = \
            CityHallNotAvailableBuildingsListView(
                self._window, defaultY=(self.__availableBuildingsListView.getCurrentY()
                                        + self.__availableBuildingsListView.getElementHeight()))
        self.__notAvailableBuildingsListView.clearElements()
        for elem in self.__notAvailableList:
            self.__notAvailableBuildingsListView.addElement(elem, False)
        self.__notAvailableBuildingsListView.drawView()

    def drawQueue(self):
        # draw queue bg
        border_rect.draw(self._window, grey44, (0, 207, 997, 108))
        self.__queueListView = CityHallQueueListView(self._window)
        self.__queueListView.clearElements()
        for elem in self.__queue:
            self.__queueListView.addElement(elem, False)
        # self.__queueListView.addElement(BuildingQueueElement("City Hall (Level 2)", 7))
        self.__queueListView.drawView()

    def disableView(self):
        self.__availableBuildingsListView.disableView()

    def updateLevel(self, level: int):
        self.__level = level

    def updateQueue(self, queue: List[BuildingQueueElement]):
        self.__queue = queue

    def updateAvailableList(self, availableList: List[AvailableBuildingElement]):
        self.__availableList = availableList

    def updateNotAvailableList(self, notAvailableList: List[NotAvailableBuildingElement]):
        self.__notAvailableList = notAvailableList

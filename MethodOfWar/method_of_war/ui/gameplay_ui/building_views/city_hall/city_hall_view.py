from mini_engine.ui.a_view import *
from method_of_war.ui.ui_global import *
from mini_engine.ui import button
from method_of_war.ui.gameplay_ui.building_views import building_header_view
from method_of_war.ui.gameplay_ui.building_views.city_hall.city_hall_queue_list_view import *
from method_of_war.ui.gameplay_ui.building_views.city_hall.city_hall_available_buildings_list_view import *
from method_of_war.ui.gameplay_ui.building_views.city_hall.city_hall_not_available_buildings_list_view import *


class CityHallView(View):
    __queueListView: CityHallQueueListView
    __availableBuildingsListView: CityHallAvailableBuildingsListView
    __notAvailableBuildingsListView: CityHallNotAvailableBuildingsListView

    # it needs to take real city hall as init argument to set up
    def drawView(self):
        # draw bg
        border_rect.draw(self._window, grey44, (0, 57, 997, 663))
        # draw building header view
        headerView = building_header_view.BuildingHeaderView(self._window, buildingColorDict["City Hall"],
                                                             "City Hall (Level 1)",
                                                             "In City Hall you can build new buildings"
                                                             " and upgrade existing ones. The higher level City Hall"
                                                             " has, the lower build times.")
        headerView.drawView()
        # draw queue list view
        self.__queueListView = CityHallQueueListView(self._window)
        self.__queueListView.addElement(BuildingQueueElement("City Hall (Level 2)", 7))
        self.__queueListView.drawView()
        # draw available buildings list view
        self.__availableBuildingsListView = CityHallAvailableBuildingsListView(self._window)
        self.__availableBuildingsListView.addElement(AvailableBuildingElement("City Hall",
                                                                              "City Hall (Level 1)",
                                                                              113, 113, 113, 11, "--> Level 2"))
        self.__availableBuildingsListView.addElement(AvailableBuildingElement("Lumber Mill",
                                                                              "Lumber Mill (Level 0)",
                                                                              113, 113, 113, 11, "--> Build"))
        self.__availableBuildingsListView.addElement(AvailableBuildingElement("Quarry",
                                                                              "Quarry (Level 0)",
                                                                              113, 113, 113, 11, "--> Build"))
        self.__availableBuildingsListView.addElement(AvailableBuildingElement("Mine",
                                                                              "Mine (Level 0)",
                                                                              113, 113, 113, 11, "--> Build"))
        self.__availableBuildingsListView.addElement(AvailableBuildingElement("Warehouse",
                                                                              "Warehouse (Level 1)",
                                                                              113, 113, 113, 11, "--> Level 2"))
        # draw not available buildings list view
        self.__notAvailableBuildingsListView = \
            CityHallNotAvailableBuildingsListView(
                self._window, defaultY=(self.__availableBuildingsListView.getCurrentY()
                                        + self.__availableBuildingsListView.getElementHeight()))
        self.__notAvailableBuildingsListView.addElement(NotAvailableBuildingElement("Barracks",
                                                                                    ["City Hall",
                                                                                     "Warehouse",
                                                                                     "Lumber Mill"],
                                                                                    [10, 7, 5]))
        self.__notAvailableBuildingsListView.drawView()

    def disableView(self):
        self.__availableBuildingsListView.disableView()

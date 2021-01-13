from mini_engine.ui.a_view import *
from method_of_war.ui.ui_global import *
from mini_engine.ui import button
from method_of_war.ui.gameplay_ui.building_views import building_header_view
from method_of_war.ui.gameplay_ui.building_views.production_buildings.production_building_list_view import *


class ProductionBuildingView(View):
    __buildingName: str
    __buildingDescription: str
    __buildingLevel: int
    __correspondingResourceDict = {
        "Lumber Mill": "wood",
        "Quarry": "granite",
        "Mine": "iron"
    }
    __currentProduction: int = 5
    __nextLevelProduction: int = 8

    def __init__(self, window, buildingName: str, buildingLevel: int):
        super().__init__(window)
        self.__buildingName = buildingName
        self.__buildingDescription = "In " + self.__buildingName + " your workers produce " \
                                     + self.__correspondingResourceDict[self.__buildingName] \
                                     + " needed for building and upgrading, " \
                                       "and also recruiting units. The higher level " \
                                     + self.__buildingName + " has, the more " \
                                     + self.__correspondingResourceDict[self.__buildingName] + " you produce."
        self.__buildingLevel = buildingLevel

    def drawView(self):
        # draw bg
        border_rect.draw(self._window, grey44, (0, 57, 997, 663))
        # draw building header view
        headerView = building_header_view.BuildingHeaderView(self._window, self.__buildingName, buildingColorDict[self.__buildingName],
                                                             self.__buildingName + " (Level " + str(
                                                                 self.__buildingLevel) + ")",
                                                             self.__buildingDescription)
        headerView.drawView()
        # draw list view
        productionListView = ProductionBuildingListView(self._window)
        productionListView.addElement(ProductionBuildingElement(self.__currentProduction, self.__nextLevelProduction))

    def updateValues(self, level: int, currentProduction: int, nextLevelProduction: int):
        self.__buildingLevel = level
        self.__currentProduction = currentProduction
        self.__nextLevelProduction = nextLevelProduction

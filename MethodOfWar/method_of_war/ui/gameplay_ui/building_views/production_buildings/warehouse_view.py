from mini_engine.ui.a_view import *
from method_of_war.ui.gameplay_ui.building_views import building_header_view
from method_of_war.ui.gameplay_ui.building_views.production_buildings.production_building_list_view import *


class WarehouseView(View):
    __buildingLevel: int
    __currentMaxStorage: int = 1000
    __nextLevelMaxStorage: int = 1229

    def __init__(self, window, buildingLevel: int):
        super().__init__(window)
        self.__buildingLevel = buildingLevel

    def drawView(self):
        # draw bg
        border_rect.draw(self._window, grey44, (0, 57, 997, 663))
        # draw building header view
        headerView = building_header_view.BuildingHeaderView(self._window, "Warehouse", buildingColorDict["Warehouse"],
                                                             "Warehouse (Level " + str(self.__buildingLevel) + ")",
                                                             "In warehouse you can store resources. "
                                                             "The higher level Warehouse has,"
                                                             " the more resources you can store.")
        headerView.drawView()
        # draw list view
        productionListView = ProductionBuildingListView(self._window, "Current maximum storage:",
                                                        "Maximum storage on next level:")
        productionListView.addElement(ProductionBuildingElement(self.__currentMaxStorage, self.__nextLevelMaxStorage))

    def updateValues(self, level: int, currentMaxCapacity: int, nextLevelMaxCapacity: int):
        self.__buildingLevel = level
        self.__currentMaxStorage = currentMaxCapacity
        self.__nextLevelMaxStorage = nextLevelMaxCapacity

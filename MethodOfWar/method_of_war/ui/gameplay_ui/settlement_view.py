import pygame
from mini_engine.ui import border_rect
from mini_engine.ui.a_view import *
from method_of_war.ui.ui_global import *
from mini_engine.ui import button
from typing import List
from method_of_war.ui.gameplay_ui.building_views.city_hall.city_hall_view import *
from method_of_war.ui.gameplay_ui.building_views.production_buildings.production_building_view import *
from method_of_war.ui.gameplay_ui.building_views.production_buildings.warehouse_view import *
from method_of_war.ui.gameplay_ui.building_views.barracks.barracks_view import *


class SettlementView(View):
    __buttonList: List[button.Button] = []
    __preClickBuildingFunction = None
    __postClickBuildingFunction = None

    __cityHallView: CityHallView
    __lumberMillView: ProductionBuildingView
    __quarryView: ProductionBuildingView
    __mineView: ProductionBuildingView
    __warehouseView: WarehouseView
    __barracksView: BarracksView

    def __init__(self, window, preClickBuildingFunction, postClickBuildingFunction):
        super().__init__(window)
        self.__preClickBuildingFunction = preClickBuildingFunction
        self.__postClickBuildingFunction = postClickBuildingFunction

        self.__cityHallView = CityHallView(self._window)
        self.__lumberMillView = ProductionBuildingView(self._window, "Lumber Mill", 1)
        self.__quarryView = ProductionBuildingView(self._window, "Quarry", 1)
        self.__mineView = ProductionBuildingView(self._window, "Mine", 1)
        self.__barracksView = BarracksView(self._window, 3)
        self.__warehouseView = WarehouseView(self._window, 2)

    def __drawBuilding(self, transform: (int, int, int, int), buildingView: View, buildingLevel: int = 3,
                       buildingColor: (int, int, int) = (64, 43, 0)):
        levelIndicatorColor = (0, 0, 0)
        borderWidth = 1
        buildingBorderColor = borderDefaultColor
        levelIndicatorBorderColor = (16, 245, 0)
        levelIndicatorWidth = 32
        levelIndicatorY = transform[1] + transform[3] - levelIndicatorWidth
        levelIndicatorTransform = (transform[0], levelIndicatorY, levelIndicatorWidth, levelIndicatorWidth)

        def addedDraw():
            border_rect.draw(self._window, levelIndicatorColor, levelIndicatorTransform, 1, levelIndicatorBorderColor)
            textSurface = getDefaultFont().render(str(buildingLevel), True, (255, 255, 255))
            self._window.blit(textSurface, (transform[0] + 11, levelIndicatorY + 5))

        buildingButton = button.Button(self._window, buildingColor, transform, borderWidth, buildingBorderColor,
                                       addedDraw=addedDraw)

        def onClick():
            self.__preClickBuildingFunction()
            buildingView.drawView()
            self.__postClickBuildingFunction(buildingView)

        buildingButton.addListener(onClick)
        buildingButton.draw()
        self.__buttonList.append(buildingButton)

    def drawView(self):
        print("drawing settlement view")
        # village view
        border_rect.draw(self._window, (44, 44, 44), (0, 57, 997, 663), 1, borderDefaultColor)

        # city hall
        self.__drawBuilding((399, 57, 200, 200), self.__cityHallView, buildingColor=buildingColorDict["City Hall"])

        # lumber mill
        self.__drawBuilding((0, 57, 128, 128), self.__lumberMillView, buildingColor=buildingColorDict["Lumber Mill"])

        # quarry
        self.__drawBuilding((0, 592, 128, 128), self.__quarryView, buildingColor=buildingColorDict["Quarry"])

        # mine
        self.__drawBuilding((869, 592, 128, 128), self.__mineView, buildingColor=buildingColorDict["Mine"])

        # barracks
        self.__drawBuilding((669, 280, 180, 180), self.__barracksView, buildingColor=buildingColorDict["Barracks"])

        # warehouse
        self.__drawBuilding((223, 403, 150, 150), self.__warehouseView, buildingColor=buildingColorDict["Warehouse"])

    def disableView(self):
        print("disabling settlement view")
        # border_rect.draw(self._window, (44, 44, 44), (0, 57, 997, 663), 1, borderDefaultColor)
        for btn in self.__buttonList:
            btn.setInteractive(False)
            btn.setReadyForDelete()
            del btn

    def getWarehouse(self) -> WarehouseView:
        return self.__warehouseView

    def getLumberMill(self) -> ProductionBuildingView:
        return self.__lumberMillView

    def getQuarry(self) -> ProductionBuildingView:
        return self.__quarryView

    def getMine(self) -> ProductionBuildingView:
        return self.__mineView

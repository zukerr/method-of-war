from method_of_war.ui.gameplay_ui.building_views.queue_building_views.city_hall.city_hall_view import *
from method_of_war.ui.gameplay_ui.building_views.production_buildings.production_building_view import *
from method_of_war.ui.gameplay_ui.building_views.production_buildings.warehouse_view import *
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.barracks.barracks_view import *
from method_of_war.enums.gameplay_view_type import GameplayViewType
import pygame


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

    def __drawBuilding(self, transform: (int, int, int, int), buildingView: View, buildingName: str, buildingLevel: int = 3,
                       buildingColor: (int, int, int) = (64, 43, 0), gameplayViewType: GameplayViewType = GameplayViewType.BUILDING):
        levelIndicatorColor = (0, 0, 0)
        borderWidth = 1
        buildingBorderColor = grey44
        levelIndicatorBorderColor = (16, 245, 0)
        levelIndicatorWidth = 32
        levelIndicatorY = transform[1] + transform[3] - levelIndicatorWidth
        levelIndicatorTransform = (transform[0], levelIndicatorY, levelIndicatorWidth, levelIndicatorWidth)

        def addedDraw():
            # TEMPORARILY TURN OFF LEVEL INDICATORS
            # border_rect.draw(self._window, levelIndicatorColor, levelIndicatorTransform, 1, levelIndicatorBorderColor)
            # textSurface = getDefaultFont().render(str(buildingLevel), True, (255, 255, 255))
            # self._window.blit(textSurface, (transform[0] + 11, levelIndicatorY + 5))

            # draw building image
            self._window.blit(buildingImageOverviewDict[buildingName], (transform[0], transform[1]))

        buildingButton = button.Button(self._window, grey44, transform, borderWidth, buildingBorderColor,
                                       addedDraw=addedDraw)

        def onClick():
            self.__preClickBuildingFunction()
            buildingView.drawView()
            self.__postClickBuildingFunction(buildingView, gameplayViewType)

        buildingButton.addListener(onClick)
        buildingButton.draw()
        self.__buttonList.append(buildingButton)

    def drawView(self):
        print("drawing settlement view")
        # village view
        border_rect.draw(self._window, (44, 44, 44), (0, 57, 997, 663), 1, borderDefaultColor)

        # city hall
        self.__drawBuilding((399, 59, 200, 200), self.__cityHallView, "City Hall", buildingColor=buildingColorDict["City Hall"],
                            gameplayViewType=GameplayViewType.CITY_HALL)

        # lumber mill
        self.__drawBuilding((2, 59, 128, 128), self.__lumberMillView, "Lumber Mill", buildingColor=buildingColorDict["Lumber Mill"])

        # quarry
        self.__drawBuilding((2, 590, 128, 128), self.__quarryView, "Quarry", buildingColor=buildingColorDict["Quarry"])

        # mine
        self.__drawBuilding((867, 590, 128, 128), self.__mineView, "Mine", buildingColor=buildingColorDict["Mine"])

        # barracks
        self.__drawBuilding((669, 280, 180, 180), self.__barracksView, "Barracks", buildingColor=buildingColorDict["Barracks"],
                            gameplayViewType=GameplayViewType.BARRACKS)

        # warehouse
        self.__drawBuilding((223, 403, 150, 150), self.__warehouseView, "Warehouse", buildingColor=buildingColorDict["Warehouse"])

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

    def getCityHall(self) -> CityHallView:
        return self.__cityHallView

    def getBarracks(self) -> BarracksView:
        return self.__barracksView

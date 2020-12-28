import pygame
from mini_engine.ui import border_rect
from mini_engine.ui.a_view import *
from method_of_war.ui.ui_global import *
from mini_engine.ui import button
from typing import List


class SettlementView(View):
    __buttonList: List[button.Button] = []

    def __drawBuilding(self, transform: (int, int, int, int), buildingLevel: int = 3,
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
        buildingButton.addListener(lambda: print("clicked a building"))
        buildingButton.draw()
        self.__buttonList.append(buildingButton)

    def drawView(self):
        print("drawing settlement view")
        # village view
        border_rect.draw(self._window, (44, 44, 44), (0, 57, 997, 663), 1, borderDefaultColor)

        # city hall
        self.__drawBuilding((399, 57, 200, 200), buildingColor=buildingColorDict["City Hall"])

        # lumber mill
        self.__drawBuilding((0, 57, 128, 128), buildingColor=buildingColorDict["Lumber Mill"])

        # quarry
        self.__drawBuilding((0, 592, 128, 128), buildingColor=buildingColorDict["Quarry"])

        # mine
        self.__drawBuilding((869, 592, 128, 128), buildingColor=buildingColorDict["Mine"])

        # barracks
        self.__drawBuilding((669, 280, 180, 180), buildingColor=buildingColorDict["Barracks"])

        # warehouse
        self.__drawBuilding((223, 403, 150, 150), buildingColor=buildingColorDict["Warehouse"])

    def disableView(self):
        print("disabling settlement view")
        # border_rect.draw(self._window, (44, 44, 44), (0, 57, 997, 663), 1, borderDefaultColor)
        for btn in self.__buttonList:
            btn.setInteractive(False)
            btn.setReadyForDelete()
            del btn

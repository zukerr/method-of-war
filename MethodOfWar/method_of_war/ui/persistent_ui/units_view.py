import pygame
from mini_engine.ui import border_rect
from method_of_war.ui.ui_global import *
from mini_engine.ui.a_view import *


class UnitsView(View):
    __maxUnitTypes: int = 11
    __currentY: int = 240
    __elementHeight: int = 24
    __currentElementCount: int = 0
    __unitsDict: dict

    def updateUnits(self, unitsDict: dict):
        self.drawView()
        self.__unitsDict = unitsDict
        if len(self.__unitsDict) > self.__maxUnitTypes:
            print("Too many units to display!")
            return
        else:
            unitNameList = list(self.__unitsDict.keys())
            self.__currentY = 240
            self.__currentElementCount = 0
            print("updating units")
            for unit in unitNameList:
                if self.__unitsDict[unit] > 0:
                    # draw element
                    self.addElement(self.__unitsDict[unit], unit)

    def addElement(self, unitQuantity: int, unitName: str):
        # element bg
        border_rect.draw(self._window, (0, 0, 0), (997, self.__currentY, 283, 24), 1, borderDefaultColor)
        # element icon
        border_rect.draw(self._window, unitColorDict[unitName], (1000, self.__currentY + 3, 18, 18), 1, borderDefaultColor)
        # setup font
        elementFont = pygame.font.SysFont('Arial', 14)
        # unit quantity
        textSurface = elementFont.render(str(unitQuantity), True, (255, 255, 255))
        self._window.blit(textSurface, (1023, self.__currentY + 3))
        # unit name
        textSurface = elementFont.render(unitName, True, (255, 255, 255))
        self._window.blit(textSurface, (1057, self.__currentY + 3))

        self.__currentY += self.__elementHeight
        self.__currentElementCount += 1

    def drawView(self):
        # units bg
        border_rect.draw(self._window, (23, 23, 23), (997, 210, 283, 293), 1, borderDefaultColor)
        # title bg
        border_rect.draw(self._window, (23, 23, 23), (997, 210, 283, 30), 1, borderDefaultColor)
        # title
        textSurface = getDefaultFont().render('Units', True, (255, 255, 255))
        self._window.blit(textSurface, (1003, 210))

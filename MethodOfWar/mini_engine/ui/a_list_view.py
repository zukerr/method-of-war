import pygame
from mini_engine.ui import border_rect
from method_of_war.ui.ui_global import *
from mini_engine.ui.a_view import *
from enum import Enum
from typing import List
from abc import *


class ListView(View, ABC):
    __maxElements: int
    __currentY: int
    _defaultY: int
    __defaultX: int
    __elementWidth: int
    _elementHeight: int
    __elementList = []
    __elementBgColor = (int, int, int)
    __listBgColor = (int, int, int)

    def __init__(self, window, maxElements: int, defaultX: int, defaultY: int, elementWidth: int, elementHeight: int,
                 elementBgColor: (int, int, int) = (0, 0, 0)):
        super().__init__(window)
        self.__maxElements = maxElements
        self.__defaultX = defaultX
        self._defaultY = defaultY
        self.__currentY = defaultY
        self.__elementWidth = elementWidth
        self._elementHeight = elementHeight
        self.__elementList = []
        self.__elementBgColor = elementBgColor

    @abstractmethod
    def _drawElementDetails(self, element, transform: (int, int, int, int)):
        pass

    def _drawViewSetup(self):
        pass

    def __resetPositions(self):
        self.__currentY = self._defaultY

    def __drawElement(self, element, transform: (int, int, int, int)):
        # draw bg
        border_rect.draw(self._window, self.__elementBgColor, transform, 1, borderDefaultColor)
        # draw details
        self._drawElementDetails(element, transform)

    def __drawAllElements(self):
        self.__resetPositions()
        for elem in self.__elementList:
            self.__drawElement(elem, (self.__defaultX, self.__currentY, self.__elementWidth, self._elementHeight))
            self.__currentY += self._elementHeight

    def addElement(self, newElement, drawImmediately: bool = True):
        if len(self.__elementList) >= self.__maxElements:
            return
        self.__elementList.append(newElement)
        if drawImmediately:
            self.drawView()

    def removeElement(self, elementToRemove, drawImmediately: bool = True):
        self.__elementList.remove(elementToRemove)
        if drawImmediately:
            self.drawView()

    def elementCount(self) -> int:
        return len(self.__elementList)

    def getCurrentY(self) -> int:
        return self.__currentY

    def getElementHeight(self) -> int:
        return self._elementHeight

    def drawView(self):
        self._drawViewSetup()
        self.__drawAllElements()

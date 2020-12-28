from mini_engine.ui.a_view import *
from abc import *


class ListViewStandard(View, ABC):
    __maxElements: int
    _elementList = []
    __elementBgColor = (int, int, int)
    __listBgColor = (int, int, int)

    def __init__(self, window, maxElements: int, elementBgColor: (int, int, int) = (0, 0, 0)):
        super().__init__(window)
        self.__maxElements = maxElements
        self._elementList = []
        self.__elementBgColor = elementBgColor

    @abstractmethod
    def _drawElementDetails(self, element, transform: (int, int, int, int)):
        pass

    @abstractmethod
    def _drawViewSetup(self):
        pass

    @abstractmethod
    def _resetPositions(self):
        pass

    def _drawElement(self, element, transform: (int, int, int, int)):
        # draw bg
        border_rect.draw(self._window, self.__elementBgColor, transform, 1, borderDefaultColor)
        # draw details
        self._drawElementDetails(element, transform)

    @abstractmethod
    def _drawAllElements(self):
        pass

    def addElement(self, newElement, drawImmediately: bool = True):
        if len(self._elementList) >= self.__maxElements:
            return
        self._elementList.append(newElement)
        if drawImmediately:
            self.drawView()

    def removeElement(self, elementToRemove, drawImmediately: bool = True):
        self._elementList.remove(elementToRemove)
        if drawImmediately:
            self.drawView()

    def elementCount(self) -> int:
        return len(self._elementList)

    def drawView(self):
        self._drawViewSetup()
        self._drawAllElements()

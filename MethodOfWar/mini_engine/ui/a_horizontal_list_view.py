from mini_engine.ui.a_list_view_standard import *
from abc import *


class HorizontalListView(ListViewStandard, ABC):
    __currentX: int
    _defaultY: int
    _defaultX: int
    _elementWidth: int
    _elementHeight: int
    __elementPadding: int

    def __init__(self, window, maxElements: int, defaultX: int, defaultY: int, elementWidth: int, elementHeight: int,
                 elementBgColor: (int, int, int) = (0, 0, 0), elementPadding: int = 8):
        super().__init__(window, maxElements, elementBgColor)
        self._defaultX = defaultX
        self._defaultY = defaultY
        self.__currentX = defaultX
        self._elementWidth = elementWidth
        self._elementHeight = elementHeight
        self.__elementPadding = elementPadding

    @abstractmethod
    def _drawElementDetails(self, element, transform: (int, int, int, int)):
        pass

    @abstractmethod
    def _drawViewSetup(self):
        pass

    def _resetPositions(self):
        self.__currentX = self._defaultX

    def _drawAllElements(self):
        self._resetPositions()
        for elem in self._elementList:
            self._drawElement(elem, (self.__currentX, self._defaultY, self._elementWidth, self._elementHeight))
            self.__currentX += self._elementWidth + self.__elementPadding

from mini_engine.ui.a_list_view_standard import *


class ListView(ListViewStandard, ABC):
    __currentY: int
    _defaultY: int
    __defaultX: int
    __elementWidth: int
    _elementHeight: int
    __elementPadding: int

    def __init__(self, window, maxElements: int, defaultX: int, defaultY: int, elementWidth: int, elementHeight: int,
                 elementBgColor: (int, int, int) = (0, 0, 0), elementPadding: int = 0):
        super().__init__(window, maxElements, elementBgColor)
        self.__defaultX = defaultX
        self._defaultY = defaultY
        self.__currentY = defaultY
        self.__elementWidth = elementWidth
        self._elementHeight = elementHeight
        self.__elementPadding = elementPadding

    @abstractmethod
    def _drawElementDetails(self, element, transform: (int, int, int, int)):
        pass

    @abstractmethod
    def _drawViewSetup(self):
        pass

    def _resetPositions(self):
        self.__currentY = self._defaultY

    def _drawAllElements(self):
        self._resetPositions()
        for elem in self._elementList:
            self._drawElement(elem, (self.__defaultX, self.__currentY, self.__elementWidth, self._elementHeight))
            self.__currentY += self._elementHeight + self.__elementPadding

    def getCurrentY(self) -> int:
        return self.__currentY

    def getElementHeight(self) -> int:
        return self._elementHeight

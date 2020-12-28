from mini_engine.ui.a_list_view import *
from method_of_war.ui.ui_global import *


class ProductionBuildingElement:
    production: int
    productionNextLevel: int

    def __init__(self, production: int, productionNextLevel: int):
        self.production = production
        self.productionNextLevel = productionNextLevel


class ProductionBuildingListView(ListView):
    __column1Name: str
    __column2Name: str

    def __init__(self, window, column1Name: str = "Production per minute",
                 column2Name: str = "Production per minute on next level"):
        super().__init__(window, maxElements=5, defaultX=0, defaultY=252, elementWidth=997, elementHeight=45)
        self.__column1Name = column1Name
        self.__column2Name = column2Name

    def _drawElementDetails(self, element: ProductionBuildingElement, transform: (int, int, int, int)):
        # current production value bg
        border_rect.draw(self._window, grey44, (transform[0], transform[1], 499, transform[3]))
        # current production value
        textSurface = getDefaultFont().render(str(element.production), True, (255, 255, 255))
        self._window.blit(textSurface, (transform[0] + 5, transform[1]))
        # next level production value bg
        border_rect.draw(self._window, grey44, (transform[0] + 499, transform[1], 498, transform[3]))
        # next level production value
        textSurface = getDefaultFont().render(str(element.productionNextLevel), True, (255, 255, 255))
        self._window.blit(textSurface, (transform[0] + 499 + 5, transform[1]))

    def _drawViewSetup(self):
        # draw title row bg
        startingY = self._defaultY - self._elementHeight
        border_rect.draw(self._window, grey44, (0, startingY, 997, self._elementHeight))
        # draw not available subtitle bg
        border_rect.draw(self._window, grey23, (0, startingY, 499, self._elementHeight))
        # draw not available subtitle
        textSurface = getDefaultFont().render(self.__column1Name, True, (255, 255, 255))
        self._window.blit(textSurface, (5, startingY))
        # draw requirements subtitle bg
        border_rect.draw(self._window, grey23, (499, startingY, 498, self._elementHeight))
        # draw requirements subtitle
        textSurface = getDefaultFont().render(self.__column2Name, True, (255, 255, 255))
        self._window.blit(textSurface, (499 + 5, startingY))

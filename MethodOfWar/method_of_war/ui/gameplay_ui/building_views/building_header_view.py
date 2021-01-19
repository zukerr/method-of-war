from mini_engine.ui import border_rect
from mini_engine.ui.a_view import *
from mini_engine.util.extensions import *


class BuildingHeaderView(View):
    __buildingIconColor: (int, int, int)
    __buildingTitle: str
    __buildingDesc: str
    __buildingName: str

    def __init__(self, window, buildingName: str, buildingColor: (int, int, int), buildingTitle: str, buildingDesc: str):
        super().__init__(window)
        self.__buildingIconColor = buildingColor
        self.__buildingTitle = buildingTitle
        self.__buildingDesc = buildingDesc
        self.__buildingName = buildingName

    def drawView(self):
        # draw header bg
        border_rect.draw(self._window, grey44, (0, 57, 997, 150))
        # draw building icon
        self._window.blit(buildingImage150pxDict[self.__buildingName], (0, 57))
        # draw building title bg
        border_rect.draw(self._window, grey44, (150, 57, 847, 50))
        # draw title
        textSurface = getVeryBigFont().render(self.__buildingTitle, True, (255, 255, 255))
        self._window.blit(textSurface, (160, 57))
        # draw details
        blit_text(self._window, (867, 100), self.__buildingDesc, (160, 107), getDefaultFont(), (255, 255, 255))

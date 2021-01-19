from mini_engine.ui import border_rect
from mini_engine.ui.a_list_view import *
from method_of_war.ui.ui_global import *
from abc import *


class BuildingListView(ListView, ABC):
    def _drawRequirementSegment(self, transform: (int, int, int, int), iconColor: (int, int, int), reqValue: str):
        # requirements wood bg
        border_rect.draw(self._window, grey44, transform)
        # requirements icon
        border_rect.draw(self._window, iconColor, (transform[0] + 5, transform[1] + 5, 35, 35))
        # requirement value
        textSurface = getDefaultFont().render(reqValue, True, (255, 255, 255))
        self._window.blit(textSurface, (transform[0] + 45, transform[1] + 5))

    def _drawBuildingInfo(self, transform: (int, int, int, int), infoText: str, infoColor: (int, int, int)):
        # building info bg
        border_rect.draw(self._window, grey44, (transform[0], transform[1], 248, transform[3]))
        # building info icon
        border_rect.draw(self._window, infoColor, (transform[0] + 5, transform[1] + 5, 35, 35))
        # building info text
        textSurface = getDefaultFont().render(infoText, True, (255, 255, 255))
        self._window.blit(textSurface, (transform[0] + 45, transform[1] + 5))

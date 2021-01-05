from mini_engine.ui.a_list_view import ListView
from mini_engine.ui import border_rect
from method_of_war.ui.ui_global import *


class ReportDetailsBgElement:
    headerColor: (int, int, int)
    headerText: str

    def __init__(self, headerColor: (int, int, int), headerText: str):
        self.headerColor = headerColor
        self.headerText = headerText


class ReportDetailsBgListView(ListView):

    def __init__(self, window):
        super().__init__(window, maxElements=14, defaultX=0, defaultY=57, elementWidth=997, elementHeight=45)

    def _drawElementDetails(self, element: ReportDetailsBgElement, transform: (int, int, int, int)):
        border_rect.draw(self._window, element.headerColor, transform)
        border_rect.draw(self._window, grey44, (transform[0] + 161, transform[1], transform[2] - 161, transform[3]))
        textSurface = getBigFont().render(element.headerText, True, (255, 255, 255))
        self._window.blit(textSurface, (transform[0] + 5, transform[1] + 5))

    def _drawViewSetup(self):
        pass

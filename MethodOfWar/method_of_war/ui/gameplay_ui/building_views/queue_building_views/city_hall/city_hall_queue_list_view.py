from mini_engine.ui import border_rect
from mini_engine.ui.a_list_view import *
from mini_engine.util.extensions import *


class BuildingQueueElement:
    taskName: str
    timeToFinish: str
    realTimeToFinish: float
    buildingName: str

    def __init__(self, taskName: str, timeToFinishInSeconds: int, realTimeToFinish: float = 0, buildingName: str = ""):
        self.taskName = taskName
        self.timeToFinish = getMinutesSecondsFromSeconds(timeToFinishInSeconds)
        self.realTimeToFinish = realTimeToFinish
        self.buildingName = buildingName


class CityHallQueueListView(ListView):
    def __init__(self, window):
        super().__init__(window, maxElements=2, defaultX=0, defaultY=237, elementWidth=997, elementHeight=39)

    def _drawElementDetails(self, element: BuildingQueueElement, transform: (int, int, int, int)):
        # draw task name bg
        border_rect.draw(self._window, grey44, (transform[0], transform[1], 786, transform[3]))
        # draw task name
        textSurface = getDefaultFont().render(element.taskName, True, (255, 255, 255))
        self._window.blit(textSurface, (transform[0] + 5, transform[1]))
        # draw time to finish bg
        border_rect.draw(self._window, grey44, (transform[0] + 786, transform[1], 211, transform[3]))
        # draw time to finish
        textSurface = getDefaultFont().render(element.timeToFinish, True, (255, 255, 255))
        self._window.blit(textSurface, (transform[0] + 791, transform[1]))
        
    def _drawViewSetup(self):
        # draw title row bg
        border_rect.draw(self._window, grey44, (0, 207, 997, 30))
        # draw building queue part bg
        border_rect.draw(self._window, grey23, (0, 207, 786, 30))
        # draw building queue text
        textSurface = getDefaultFont().render("Building Queue", True, (255, 255, 255))
        self._window.blit(textSurface, (5, 207))
        # draw time to finish part bg
        border_rect.draw(self._window, grey23, (786, 207, 211, 30))
        # draw time to finish text
        textSurface = getDefaultFont().render("Time to finish", True, (255, 255, 255))
        self._window.blit(textSurface, (791, 207))

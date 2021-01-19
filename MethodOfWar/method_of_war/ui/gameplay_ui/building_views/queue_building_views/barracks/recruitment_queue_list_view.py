from mini_engine.ui import border_rect
from mini_engine.ui.a_horizontal_list_view import *
from method_of_war.ui.ui_global import *
from mini_engine.util.extensions import *


class RecruitmentQueueElement:
    timeToFinish: str
    bgColor: (int, int, int)
    # from 0 to 1
    progressBarProgress: float
    darkText: bool
    realTimeToFinish: float
    __originalRealTimeToFinish: float

    def __init__(self, timeToFinishInSeconds: int, bgColor: (int, int, int), progressBarProgress: float,
                 makeTextDark: bool = False, realTimeToFinish: float = 0):
        self.timeToFinish = getMinutesSecondsFromSeconds(timeToFinishInSeconds)
        self.bgColor = bgColor
        self.progressBarProgress = progressBarProgress
        self.darkText = makeTextDark
        self.realTimeToFinish = realTimeToFinish
        self.__originalRealTimeToFinish = self.realTimeToFinish

    def updateTimeToFinish(self):
        self.timeToFinish = getMinutesSecondsFromSeconds(int(self.realTimeToFinish))
        self.progressBarProgress = 1 - (self.realTimeToFinish / self.__originalRealTimeToFinish)


class RecruitmentQueueListView(HorizontalListView):
    def __init__(self, window):
        super().__init__(window, maxElements=8, defaultX=5, defaultY=257, elementWidth=115, elementHeight=71,
                         elementBgColor=grey44)

    def _drawElementDetails(self, element: RecruitmentQueueElement, transform: (int, int, int, int)):
        # draw unit color bg
        border_rect.draw(self._window, element.bgColor, transform)
        # draw time to finish
        # setup color
        textColor = (255, 255, 255)
        if element.darkText:
            textColor = (0, 0, 0)
        textSurface = getVeryBigFont().render(element.timeToFinish, True, textColor)
        self._window.blit(textSurface, (transform[0] + 4, transform[1] + 14))
        # draw progress bar
        # bg
        border_rect.draw(self._window, (0, 0, 0), (transform[0], transform[1] + 60, transform[2], 11))
        # progress
        if element.progressBarProgress > 0:
            progressWidth = element.progressBarProgress * transform[2]
            border_rect.draw(self._window, defaultGreen, (transform[0], transform[1] + 60, int(progressWidth), 11))

    def _drawViewSetup(self):
        startingY = 207
        # draw title bg
        border_rect.draw(self._window, grey23, (0, startingY, 997, 45))
        # draw title
        textSurface = getDefaultFont().render("Recruitment Queue", True, (255, 255, 255))
        self._window.blit(textSurface, (5, startingY))

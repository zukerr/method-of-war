from mini_engine.ui import border_rect
from mini_engine.ui.a_horizontal_list_view import *
from method_of_war.ui.ui_global import *


class RecruitmentQueueBgElement:
    placementNumber: int

    def __init__(self, placementNumber: int):
        self.placementNumber = placementNumber


class RecruitmentQueueBgListView(HorizontalListView):
    def __init__(self, window):
        super().__init__(window, maxElements=8, defaultX=5, defaultY=257, elementWidth=115, elementHeight=71,
                         elementBgColor=grey44)

    def _drawElementDetails(self, element: RecruitmentQueueBgElement, transform: (int, int, int, int)):
        # draw element number
        textSurface = getVeryBigFont().render(str(element.placementNumber), True, (255, 255, 255))
        self._window.blit(textSurface, (transform[0] + 48, transform[1] + 14))

    def _drawViewSetup(self):
        startingY = 207
        # draw title bg
        border_rect.draw(self._window, grey23, (0, startingY, 997, 45))
        # draw title
        textSurface = getDefaultFont().render("Recruitment Queue", True, (255, 255, 255))
        self._window.blit(textSurface, (5, startingY))

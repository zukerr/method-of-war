from mini_engine.ui.a_view import *
from mini_engine.ui import button
import pygame
from abc import *
from method_of_war.core.levels import global_level


class GameResultView(View, ABC):
    __gameResultStr: str
    __gameResultCaps: str
    __gameResultTextX: int

    def __init__(self, window, gameResultStr: str, gameResultCaps: str, gameResultTextX: int):
        super().__init__(window)
        self.__gameResultStr = gameResultStr
        self.__gameResultCaps = gameResultCaps
        self.__gameResultTextX = gameResultTextX

    def drawView(self):
        # draw bg
        border_rect.draw(self._window, grey44, (0, 0, 1280, 720))
        # draw victory bg
        frameTransform = (265, 166, 750, 256)
        border_rect.draw(self._window, grey23, frameTransform)
        # draw victory frame
        self._window.blit(gameResultFrameDict[self.__gameResultStr], (frameTransform[0], frameTransform[1]))
        # draw victory text
        textSurface = getFontSize100().render(self.__gameResultCaps, True, (255, 255, 255))
        self._window.blit(textSurface, (self.__gameResultTextX, 227))

        # draw continue button
        def addedDraw():
            textSurface = getVeryBigFont().render("CONTINUE", True, (255, 255, 255))
            self._window.blit(textSurface, (557, 565))

        def onClick():
            global_level.levelIsRunning = False

        buttonContinue = button.Button(self._window, (0, 0, 0), (493, 541, 294, 94), 5, borderDefaultColor,
                                       addedDraw=addedDraw)
        buttonContinue.addListener(onClick)
        buttonContinue.draw()

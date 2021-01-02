from mini_engine.ui.button import Button
import pygame
from method_of_war.ui.ui_global import *


class GreenButton(Button):
    def __init__(self, window: pygame.display, transform: (int, int, int, int), text: str, font: pygame.font):
        def addedDraw():
            # build button text
            textSurface = font.render(text, True, (255, 255, 255))
            self._window.blit(textSurface, (transform[0] + 6, transform[1]))

        super().__init__(window, darkGreen, transform, 1, borderDefaultColor, addedDraw=addedDraw)


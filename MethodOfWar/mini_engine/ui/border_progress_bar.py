import pygame
from mini_engine.ui import border_rect


def draw(window: pygame.display,
         transform: (int, int, int, int),
         fillAmount: float = 1,
         textValue: str = "",
         font: pygame.font = None,
         textColor: (int, int, int) = (255, 255, 255),
         fillColor: (int, int, int) = (104, 0, 0),
         backgroundColor: (int, int, int) = (0, 0, 0),
         borderWidth: int = 1,
         borderColor: (int, int, int) = (112, 112, 112)):
    # draw bar bg
    border_rect.draw(window, backgroundColor, transform, borderWidth, borderColor)
    # calculate bar width
    barWidth: float = fillAmount * transform[2]
    barTransform = (transform[0], transform[1], int(barWidth), transform[3])
    # draw bar
    border_rect.draw(window, fillColor, barTransform, borderWidth, borderColor)
    # draw text
    if textValue != "":
        textSurface = font.render(textValue, True, textColor)
        window.blit(textSurface, (transform[0] + 6, transform[1]))

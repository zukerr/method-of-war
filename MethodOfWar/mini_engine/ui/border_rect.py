import pygame


def draw(window: pygame.display, color: (int, int, int), transform: (int, int, int, int),
         borderWidth: int = 1, borderColor: (int, int, int) = (112, 112, 112)):
    pygame.draw.rect(window, borderColor, transform)
    pygame.draw.rect(window, color,
                     (transform[0] + borderWidth,
                      transform[1] + borderWidth,
                      transform[2] - 2 * borderWidth,
                      transform[3] - 2 * borderWidth))

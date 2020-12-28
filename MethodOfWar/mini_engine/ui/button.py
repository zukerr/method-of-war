import pygame
from mini_engine.game_machine.a_mono_behaviour import MonoBehaviour
from mini_engine.ui import border_rect


class Button(MonoBehaviour):
    __window: pygame.display
    __color: (int, int, int)
    __transform: (int, int, int, int)
    __borderWidth: int
    __borderColor: (int, int, int)
    __highlightColor: (int, int, int)
    __addedDraw = lambda: None
    __buttonListener = lambda: None
    __interactive = True
    __readyToDelete = False

    def __init__(self, window: pygame.display, color: (int, int, int), transform: (int, int, int, int),
                 borderWidth: int, borderColor: (int, int, int), highlightColor: (int, int, int) = (80, 80, 80),
                 addedDraw=lambda: None, interactive=True):
        super().__init__()
        self.__window = window
        self.__color = color
        self.__transform = transform
        self.__borderWidth = borderWidth
        self.__borderColor = borderColor
        self.__highlightColor = highlightColor
        self.__addedDraw = addedDraw
        self.__interactive = interactive

    def draw(self):
        border_rect.draw(self.__window, self.__color, self.__transform, self.__borderWidth, self.__borderColor)
        self.__drawText()
        self.__addedDraw()

    def addListener(self, listener=lambda: None):
        self.__buttonListener = listener

    def setInteractive(self, value: bool):
        self.__interactive = value

    def __drawText(self):
        pass

    def __onMouseEnter(self):
        border_rect.draw(self.__window, self.__highlightColor, self.__transform, self.__borderWidth, self.__borderColor)
        self.__drawText()
        self.__addedDraw()

    def __onMouseExit(self):
        self.draw()

    def __isMouseOver(self, mousePosition: (int, int)) -> bool:
        if self.__transform[0] < mousePosition[0] < (self.__transform[0] + self.__transform[2]):
            if self.__transform[1] < mousePosition[1] < (self.__transform[1] + self.__transform[3]):
                return True
        return False

    def setReadyForDelete(self):
        self.__readyToDelete = True

    def start(self):
        pass

    def update(self):
        if not self.__readyToDelete:
            self.draw()
            mousePosition = pygame.mouse.get_pos()
            if self.__interactive:
                if self.__isMouseOver(mousePosition):
                    self.__onMouseEnter()
                else:
                    self.__onMouseExit()

    def updateOnEvent(self, event: pygame.event):
        if not self.__readyToDelete:
            super().updateOnEvent(event)
            mousePosition = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__interactive:
                    if self.__isMouseOver(mousePosition):
                        self.__buttonListener()

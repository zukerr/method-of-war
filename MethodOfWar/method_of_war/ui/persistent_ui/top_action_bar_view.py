from mini_engine.ui import button
from mini_engine.ui.a_view import *
from method_of_war.enums.gameplay_view_type import *
from method_of_war.ui import global_gameplay_view_manager
import pygame


class TopActionBarView(View):
    __buttonNameToViewTypeDict = {
        "Overview": GameplayViewType.OVERVIEW,
        "Map": GameplayViewType.MAP,
        "Reports": GameplayViewType.REPORTS
    }
    __timerText: str = "00:00"

    def __drawSegment(self,
                      buttonColor: (int, int, int),
                      buttonTransform: (int, int, int, int),
                      borderColor: (int, int, int),
                      iconColor: (int, int, int),
                      iconTransform: (int, int, int, int),
                      font: pygame.font,
                      textValue: str,
                      textPosition: (int, int)):
        border_rect.draw(self._window, buttonColor, buttonTransform, 1, borderColor)
        border_rect.draw(self._window, iconColor, iconTransform, 1, borderColor)
        textSurface = font.render(textValue, True, (255, 255, 255))
        self._window.blit(textSurface, textPosition)

    def __drawButtonSegment(self,
                            buttonColor: (int, int, int),
                            buttonTransform: (int, int, int, int),
                            borderColor: (int, int, int),
                            iconColor: (int, int, int),
                            iconTransform: (int, int, int, int),
                            font: pygame.font,
                            textValue: str,
                            textPosition: (int, int)):
        def addedDraw():
            border_rect.draw(self._window, iconColor, iconTransform, 1, borderColor)
            textSurface = font.render(textValue, True, (255, 255, 255))
            self._window.blit(textSurface, textPosition)

        def onClick():
            print("just clicked " + textValue)
            global_gameplay_view_manager.globalGameplayViewManager.switchGameplayView(self.__buttonNameToViewTypeDict[textValue])

        segmentButton = button.Button(self._window, buttonColor, buttonTransform, 1, borderColor, addedDraw=addedDraw)
        segmentButton.addListener(onClick)
        segmentButton.draw()

    def drawView(self):
        # bar bg
        border_rect.draw(self._window, (23, 23, 23), (0, 0, 1280, 57), 1, borderDefaultColor)

        # action buttons section
        actionButtonColor = (48, 48, 48)
        # overview button
        self.__drawButtonSegment(actionButtonColor, (10, 8, 126, 41), borderDefaultColor, iconTempColor,
                                 (15, 14, 30, 30),
                                 getDefaultFont(), 'Overview', (52, 14))

        # map button
        self.__drawButtonSegment(actionButtonColor, (146, 8, 126, 41), borderDefaultColor, iconTempColor,
                                 (151, 14, 30, 30),
                                 getDefaultFont(), 'Map', (188, 14))

        # reports button
        self.__drawButtonSegment(actionButtonColor, (282, 8, 126, 41), borderDefaultColor, iconTempColor,
                                 (287, 14, 30, 30),
                                 getDefaultFont(), 'Reports', (324, 14))

        # resources section
        resourceSegmentColor = (48, 48, 48)
        # wood
        self.__drawSegment(resourceSegmentColor, (906, 8, 91, 41), borderDefaultColor, resourceColorDict["Wood"],
                           (909, 11, 27, 35),
                           getDefaultFont(), '531', (943, 13))

        # granite
        self.__drawSegment(resourceSegmentColor, (997, 8, 91, 41), borderDefaultColor, resourceColorDict["Granite"],
                           (1000, 11, 27, 35),
                           getDefaultFont(), '965', (1034, 13))

        # iron
        self.__drawSegment(resourceSegmentColor, (1088, 8, 91, 41), borderDefaultColor, resourceColorDict["Iron"],
                           (1091, 11, 27, 35),
                           getDefaultFont(), '127', (1125, 13))

        # max capacity
        self.__drawSegment(resourceSegmentColor, (1179, 8, 91, 41), borderDefaultColor, resourceColorDict["All"],
                           (1182, 11, 27, 35),
                           getDefaultFont(), '1000', (1216, 13))

        # timer
        pygame.draw.rect(self._window, grey23, (813, 8, 81, 41))
        textSurface = getBigFont().render(self.__timerText, True, (255, 255, 255))
        self._window.blit(textSurface, (826, 13))

    def updateTimerText(self, newTimerText: str):
        self.__timerText = newTimerText
        pygame.draw.rect(self._window, grey23, (813, 8, 81, 41))
        textSurface = getBigFont().render(self.__timerText, True, (255, 255, 255))
        self._window.blit(textSurface, (826, 13))

    def updateWoodText(self, newWoodText: str):
        resourceSegmentColor = (48, 48, 48)
        # wood
        self.__drawSegment(resourceSegmentColor, (906, 8, 91, 41), borderDefaultColor, resourceColorDict["Wood"],
                           (909, 11, 27, 35),
                           getDefaultFont(), newWoodText, (943, 13))

    def updateGraniteText(self, newGraniteText: str):
        resourceSegmentColor = (48, 48, 48)
        # granite
        self.__drawSegment(resourceSegmentColor, (997, 8, 91, 41), borderDefaultColor, resourceColorDict["Granite"],
                           (1000, 11, 27, 35),
                           getDefaultFont(), newGraniteText, (1034, 13))

    def updateIronText(self, newIronText: str):
        resourceSegmentColor = (48, 48, 48)
        # iron
        self.__drawSegment(resourceSegmentColor, (1088, 8, 91, 41), borderDefaultColor, resourceColorDict["Iron"],
                           (1091, 11, 27, 35),
                           getDefaultFont(), newIronText, (1125, 13))

    def updateMaxResourcesText(self, newMaxResourcesText: str):
        resourceSegmentColor = (48, 48, 48)
        # max capacity
        self.__drawSegment(resourceSegmentColor, (1179, 8, 91, 41), borderDefaultColor, resourceColorDict["All"],
                           (1182, 11, 27, 35),
                           getDefaultFont(), newMaxResourcesText, (1216, 13))

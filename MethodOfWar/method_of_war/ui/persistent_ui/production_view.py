import pygame
from mini_engine.ui import border_rect
from method_of_war.ui.ui_global import *
from mini_engine.ui.a_view import *


class ProductionView(View):

    __woodValue: int = 0
    __graniteValue: int = 0
    __ironValue: int = 0

    def updateProductionValues(self, woodValue: int = 0, graniteValue: int = 0, ironValue: int = 0):
        if woodValue != 0:
            self.__woodValue = woodValue
        if graniteValue != 0:
            self.__graniteValue = graniteValue
        if ironValue != 0:
            self.__ironValue = ironValue
        self.drawView()

    def __drawProductionSegment(self,
                                backgroundTransform,
                                iconSectionTransform,
                                iconTransform,
                                valueSectionTransform,
                                iconSectionText,
                                iconSectionTextTransform,
                                valueText,
                                valueTextTransform,
                                iconColor=iconTempColor):
        # segment bg
        border_rect.draw(self._window, (0, 0, 0), backgroundTransform, 1, borderDefaultColor)
        # icon section bg
        border_rect.draw(self._window, (0, 0, 0), iconSectionTransform, 1, borderDefaultColor)
        # icon
        border_rect.draw(self._window, iconColor, iconTransform, 1, borderDefaultColor)
        # icon text
        textSurface = getDefaultFont().render(iconSectionText, True, (255, 255, 255))
        self._window.blit(textSurface, iconSectionTextTransform)
        # value section bg
        border_rect.draw(self._window, (0, 0, 0), valueSectionTransform, 1, borderDefaultColor)
        # value text
        textSurface = getDefaultFont().render(valueText + ' per minute', True, (255, 255, 255))
        self._window.blit(textSurface, valueTextTransform)

    def drawView(self):
        # view bg
        border_rect.draw(self._window, (23, 23, 23), (997, 57, 283, 153), 1, borderDefaultColor)

        # title bg
        border_rect.draw(self._window, (23, 23, 23), (997, 57, 283, 30), 1, borderDefaultColor)

        # title
        textSurface = getDefaultFont().render('Production', True, (255, 255, 255))
        self._window.blit(textSurface, (1003, 57))

        # segments
        self.__drawProductionSegment(backgroundTransform=(997, 87, 283, 41),
                                     iconSectionTransform=(997, 87, 108, 41),
                                     iconTransform=(1000, 90, 27, 35),
                                     valueSectionTransform=(1105, 87, 175, 41),
                                     iconSectionText='Wood',
                                     iconSectionTextTransform=(1032, 93),
                                     valueText=str(self.__woodValue),
                                     valueTextTransform=(1110, 90),
                                     iconColor=resourceColorDict["Wood"])
        self.__drawProductionSegment(backgroundTransform=(997, 128, 283, 41),
                                     iconSectionTransform=(997, 128, 108, 41),
                                     iconTransform=(1000, 131, 27, 35),
                                     valueSectionTransform=(1105, 128, 175, 41),
                                     iconSectionText='Granite',
                                     iconSectionTextTransform=(1032, 134),
                                     valueText=str(self.__graniteValue),
                                     valueTextTransform=(1110, 131),
                                     iconColor=resourceColorDict["Granite"])
        self.__drawProductionSegment(backgroundTransform=(997, 169, 283, 41),
                                     iconSectionTransform=(997, 169, 108, 41),
                                     iconTransform=(1000, 172, 27, 35),
                                     valueSectionTransform=(1105, 169, 175, 41),
                                     iconSectionText='Iron',
                                     iconSectionTextTransform=(1032, 175),
                                     valueText=str(self.__ironValue),
                                     valueTextTransform=(1110, 172),
                                     iconColor=resourceColorDict["Iron"])

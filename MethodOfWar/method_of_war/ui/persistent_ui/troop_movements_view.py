import pygame
from mini_engine.ui import border_rect
from method_of_war.ui.ui_global import *
from mini_engine.ui.a_view import *
from mini_engine.ui.a_list_view import *
from typing import List
from method_of_war.enums.attack_size import *
from mini_engine.util.extensions import *


class TroopMovementElement:
    attackSize: AttackSize
    fromEnemy: bool
    attackingSettlement: str
    defendingSettlement: str
    secondsToBattle: int

    def __init__(self, attackSize: AttackSize, fromEnemy: bool, attackingSettlement: str, defendingSettlement: str,
                 secondsToBattle: int):
        self.attackSize = attackSize
        self.fromEnemy = fromEnemy
        self.attackingSettlement = attackingSettlement
        self.defendingSettlement = defendingSettlement
        self.secondsToBattle = secondsToBattle


class TroopMovementsView(ListView):

    def __init__(self, window):
        super().__init__(window, maxElements=7, defaultX=997, defaultY=533, elementWidth=283, elementHeight=24)

    def _drawElementDetails(self, element: TroopMovementElement, transform: (int, int, int, int)):
        # draw attack size icon
        attackColor = attackSizeColorDict[element.attackSize]
        border_rect.draw(self._window, attackColor, (1000, transform[1] + 3, 18, 18), 1, borderDefaultColor)

        # draw attack string
        textSurface = getSmallFont().render(element.attackingSettlement + ' -> ' + element.defendingSettlement, True,
                                            (255, 255, 255))
        self._window.blit(textSurface, (1024, transform[1] + 3))

        # draw enemy indicator
        colorRed = defaultRed
        colorGreen = defaultGreen
        actualIndicatorColor = colorGreen
        if element.fromEnemy:
            actualIndicatorColor = colorRed
        border_rect.draw(self._window, actualIndicatorColor, (1199, transform[1] + 3, 39, 18), 1, borderDefaultColor)

        # draw seconds to battle
        textToDisplay = getMinutesSecondsFromSeconds(element.secondsToBattle)
        textSurface = getSmallFont().render(textToDisplay, True, (255, 255, 255))
        self._window.blit(textSurface, (1242, transform[1] + 3))

    def _drawViewSetup(self):
        # units bg
        border_rect.draw(self._window, (23, 23, 23), (997, 503, 283, 217), 1, borderDefaultColor)
        # title bg
        border_rect.draw(self._window, (23, 23, 23), (997, 503, 283, 30), 1, borderDefaultColor)
        # title
        textSurface = getDefaultFont().render('Troop Movements', True, (255, 255, 255))
        self._window.blit(textSurface, (1003, 503))

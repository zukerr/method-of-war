import pygame
from mini_engine.ui import border_rect
from mini_engine.ui.a_view import *
from mini_engine.ui.a_list_view import *
from method_of_war.ui.ui_global import *
from mini_engine.ui import button
from method_of_war.ui.persistent_ui.troop_movements_view import AttackSize
from method_of_war.enums.battle_result import *
from mini_engine.util.extensions import *


class ReportElement:
    battleResult: BattleResult
    attackSize: AttackSize
    attackingPlayerName: str
    attackingSettlementName: str
    defendingSettlementName: str
    attackingSettlementLocation: (int, int)
    defendingSettlementLocation: (int, int)
    timestampInSeconds: int

    def __init__(self, battleResult: BattleResult, attackSize: AttackSize, attackingPlayerName: str,
                 attackingSettlementName: str,
                 defendingSettlementName: str, attackingSettlementLocation: (int, int),
                 defendingSettlementLocation: (int, int),
                 timestampInSeconds: int):
        self.battleResult = battleResult
        self.attackSize = attackSize
        self.attackingPlayerName = attackingPlayerName
        self.attackingSettlementName = attackingSettlementName
        self.defendingSettlementName = defendingSettlementName
        self.attackingSettlementLocation = attackingSettlementLocation
        self.defendingSettlementLocation = defendingSettlementLocation
        self.timestampInSeconds = timestampInSeconds


class ReportsView(ListView):
    def __init__(self, window):
        super().__init__(window, maxElements=13, defaultX=0, defaultY=102, elementWidth=997, elementHeight=45,
                         elementBgColor=grey44)

    def _drawElementDetails(self, element: ReportElement, transform: (int, int, int, int)):
        # battle result icon
        battleResultColor = battleResultColorDict[element.battleResult]
        border_rect.draw(self._window, battleResultColor, (transform[0] + 5, transform[1] + 5, 35, 35), 1,
                         borderDefaultColor)
        # report topic
        textToDisplay = element.attackingPlayerName + " (" + element.attackingSettlementName + " (" \
                        + str(element.attackingSettlementLocation[0]) \
                        + ", " + str(element.attackingSettlementLocation[1]) \
                        + ")) attacks " + element.defendingSettlementName \
                        + " (" + str(element.defendingSettlementLocation[0]) + ", " \
                        + str(element.defendingSettlementLocation[1]) + ")"
        textSurface = getBigFont().render(textToDisplay, True, (255, 255, 255))
        self._window.blit(textSurface, (transform[0] + 47, transform[1] + 5))
        # attack size indicator
        battleResultColor = attackSizeColorDict[element.attackSize]
        border_rect.draw(self._window, battleResultColor, (transform[0] + 883, transform[1] + 5, 35, 35), 1,
                         borderDefaultColor)
        # timestamp bg
        border_rect.draw(self._window, grey44, (transform[0] + 923, transform[1], 74, 45), 1, borderDefaultColor)
        # timestamp
        textSurface = getBigFont().render(getMinutesSecondsFromSeconds(element.timestampInSeconds), True, (255, 255, 255))
        self._window.blit(textSurface, (transform[0] + 931, transform[1] + 5))

    def _drawViewSetup(self):
        # bg
        border_rect.draw(self._window, (23, 23, 23), (0, 57, 997, 663), 1, borderDefaultColor)
        # title bg
        border_rect.draw(self._window, (44, 44, 44), (0, 57, 997, 45), 1, borderDefaultColor)
        # title
        textSurface = getBigFont().render('Topic', True, (255, 255, 255))
        self._window.blit(textSurface, (5, 62))
        # timestamp column bg
        border_rect.draw(self._window, (44, 44, 44), (923, 57, 74, 45), 1, borderDefaultColor)
        # timestamp text
        textSurface = getBigFont().render('Time', True, (255, 255, 255))
        self._window.blit(textSurface, (931, 62))

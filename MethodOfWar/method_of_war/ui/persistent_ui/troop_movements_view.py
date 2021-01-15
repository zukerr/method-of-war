import pygame
from mini_engine.ui import border_rect
from method_of_war.ui.ui_global import *
from mini_engine.ui.a_view import *
from mini_engine.ui.a_list_view import *
from typing import List
from method_of_war.enums.attack_size import *
from mini_engine.util.extensions import *
from method_of_war.ui import ui_global


class TroopMovementElement:
    attackSize: AttackSize
    fromEnemy: bool
    attackingSettlement: str
    defendingSettlement: str
    secondsToBattle: int
    realTimeToFinish: float
    attackingArmy: dict
    defendingArmy: dict
    isRetreating: bool
    originalRealTimeToFinish: float
    attackingPlayer: str
    defendingPlayer: str
    attackingSettlementLocation: (int, int)
    defendingSettlementLocation: (int, int)
    elemId: int
    carriedWood: int
    carriedGranite: int
    carriedIron: int

    def __init__(self, attackSize: AttackSize, fromEnemy: bool, attackingSettlement: str, defendingSettlement: str,
                 secondsToBattle: int, realTimeToFinish: float = 0, attackingArmy: dict = None,
                 defendingArmy: dict = None, isRetreating: bool = False, attackingPlayer: str = "",
                 defendingPlayer: str = "", attackingSettlementLocation: (int, int) = (-1, -1),
                 defendingSettlementLocation: (int, int) = (-1, -1), elemId: int = 0,
                 carriedWood: int = 0, carriedGranite: int = 0, carriedIron: int = 0):
        if defendingArmy is None:
            defendingArmy = {}
        if attackingArmy is None:
            attackingArmy = {}
        self.attackingArmy = attackingArmy
        self.defendingArmy = defendingArmy
        self.attackSize = attackSize
        self.fromEnemy = fromEnemy
        self.attackingSettlement = attackingSettlement
        self.defendingSettlement = defendingSettlement
        self.secondsToBattle = secondsToBattle
        self.realTimeToFinish = realTimeToFinish
        self.isRetreating = isRetreating
        self.originalRealTimeToFinish = realTimeToFinish
        self.attackingPlayer = attackingPlayer
        self.defendingPlayer = defendingPlayer
        self.attackingSettlementLocation = attackingSettlementLocation
        self.defendingSettlementLocation = defendingSettlementLocation
        self.elemId = elemId
        self.carriedWood = carriedWood
        self.carriedGranite = carriedGranite
        self.carriedIron = carriedIron

    def modifyRealTimeToFinish(self, newValue: float):
        self.realTimeToFinish = newValue
        self.secondsToBattle = int(self.realTimeToFinish)

    def getCopy(self):
        copy = TroopMovementElement(
            self.attackSize,
            self.fromEnemy,
            self.attackingSettlement,
            self.defendingSettlement,
            self.secondsToBattle,
            self.realTimeToFinish,
            self.attackingArmy,
            self.defendingArmy,
            self.isRetreating,
            self.attackingPlayer,
            self.defendingPlayer,
            self.attackingSettlementLocation,
            self.defendingSettlementLocation,
            self.elemId
        )
        copy.originalRealTimeToFinish = self.originalRealTimeToFinish
        return copy


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
        if element.isRetreating:
            actualIndicatorColor = (0, 0, 0)
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

    def updateElementsList(self, elementList: List[TroopMovementElement]):
        self._elementList = elementList

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
    defendingPlayerName: str
    attackingSettlementName: str
    defendingSettlementName: str
    attackingSettlementLocation: (int, int)
    defendingSettlementLocation: (int, int)
    timestampInSeconds: int
    timestampStr: str
    buttonListener = lambda x: None
    topicToDisplay: str
    resultString: str
    attackingSettlementLocationStr: str
    defendingSettlementLocationStr: str
    initialAttackingArmyDict: dict
    attackingArmyLossesDict: dict
    initialDefendingArmyDict: dict
    defendingArmyLossesDict: dict
    lootedWood: int
    lootedGranite: int
    lootedIron: int
    lootSummary: int
    lootingCapacity: int
    isFailedAttack: bool
    attackingArmyWon: bool

    def __init__(self,
                 battleResult: BattleResult,
                 attackSize: AttackSize,
                 attackingPlayerName: str,
                 defendingPlayerName: str,
                 attackingSettlementName: str,
                 defendingSettlementName: str, attackingSettlementLocation: (int, int),
                 defendingSettlementLocation: (int, int),
                 timestampInSeconds: int,
                 initialAttackingArmyDict: dict,
                 attackingArmyLossesDict: dict,
                 initialDefendingArmyDict: dict,
                 defendingArmyLossesDict: dict,
                 buttonListener=lambda x: None,
                 lootedWood: int = 0,
                 lootedGranite: int = 0,
                 lootedIron: int = 0,
                 lootSummary: int = 0,
                 lootingCapacity: int = 0,
                 isFailedAttack: bool = False,
                 attackingArmyWon: bool = True):
        self.battleResult = battleResult
        self.attackSize = attackSize
        self.attackingPlayerName = attackingPlayerName
        self.defendingPlayerName = defendingPlayerName
        self.attackingSettlementName = attackingSettlementName
        self.defendingSettlementName = defendingSettlementName
        self.attackingSettlementLocation = attackingSettlementLocation
        self.defendingSettlementLocation = defendingSettlementLocation
        self.timestampInSeconds = timestampInSeconds
        self.buttonListener = buttonListener
        self.attackingSettlementLocationStr = "(" \
                                              + str(attackingSettlementLocation[0]) \
                                              + ", " + str(attackingSettlementLocation[1]) \
                                              + ")"
        self.defendingSettlementLocationStr = "(" \
                                              + str(defendingSettlementLocation[0]) \
                                              + ", " + str(defendingSettlementLocation[1]) \
                                              + ")"
        self.topicToDisplay = attackingPlayerName + " " \
                              + self.attackingSettlementLocationStr \
                              + " attacks " + defendingPlayerName \
                              + " " + self.defendingSettlementLocationStr
        self.timestampStr = getMinutesSecondsFromSeconds(timestampInSeconds)
        self.initialAttackingArmyDict = initialAttackingArmyDict
        self.attackingArmyLossesDict = attackingArmyLossesDict
        self.initialDefendingArmyDict = initialDefendingArmyDict
        self.defendingArmyLossesDict = defendingArmyLossesDict
        self.lootedWood = lootedWood
        self.lootedGranite = lootedGranite
        self.lootedIron = lootedIron
        self.lootSummary = lootSummary
        self.lootingCapacity = lootingCapacity
        self.isFailedAttack = isFailedAttack
        self.attackingArmyWon = attackingArmyWon
        if self.attackingArmyWon:
            self.resultString = attackingPlayerName + " won"
        else:
            self.resultString = defendingPlayerName + " won"


class ReportsListView(ListView):
    __reportButtons: List[button.Button]

    def __init__(self, window):
        self.__reportButtons = []
        super().__init__(window, maxElements=13, defaultX=0, defaultY=102, elementWidth=997, elementHeight=45,
                         elementBgColor=grey44)

    def _drawElementDetails(self, element: ReportElement, transform: (int, int, int, int)):
        def addedDraw():
            # battle result icon
            battleResultColor = battleResultColorDict[element.battleResult]
            border_rect.draw(self._window, battleResultColor, (transform[0] + 5, transform[1] + 5, 35, 35), 1,
                             borderDefaultColor)
            # report topic
            textToDisplay = element.topicToDisplay
            textSurface = getBigFont().render(textToDisplay, True, (255, 255, 255))
            self._window.blit(textSurface, (transform[0] + 47, transform[1] + 5))
            # attack size indicator
            attackSizeColor = attackSizeColorDict[element.attackSize]
            border_rect.draw(self._window, attackSizeColor, (transform[0] + 883, transform[1] + 5, 35, 35), 1,
                             borderDefaultColor)
            # timestamp bg
            border_rect.draw(self._window, grey44, (transform[0] + 923, transform[1], 74, 45), 1, borderDefaultColor)
            # timestamp
            textSurface = getBigFont().render(element.timestampStr, True, (255, 255, 255))
            self._window.blit(textSurface, (transform[0] + 931, transform[1] + 5))

        def onClick():
            print("Clicked a report!")
            element.buttonListener(element)

        reportButton = button.Button(self._window, grey44, transform, 1, borderDefaultColor, addedDraw=addedDraw)
        reportButton.addListener(onClick)
        reportButton.draw()
        self.__reportButtons.append(reportButton)

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

    def disableView(self):
        for btn in self.__reportButtons:
            btn.setActive(False)
            btn.setReadyForDelete()

    def updateElementsList(self, elementList: List[ReportElement]):
        self._elementList = elementList

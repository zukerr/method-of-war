# t = s/v
# example speed: 0.1 units per second
from mini_engine.game_machine.a_passing_time_aware_mono_behaviour import PassingTimeAwareMonoBehaviour
from method_of_war.ui.persistent_ui.troop_movements_view import TroopMovementElement
from method_of_war.ui.gameplay_ui.reports.reports_list_view import ReportElement
from typing import List
from method_of_war.core.attacks.battle import *
from method_of_war.enums.battle_result import BattleResult


class TroopMovements(PassingTimeAwareMonoBehaviour):
    _elementsList: List[TroopMovementElement] = []
    __maxListLength: int
    __rootSettlement = None
    __currentTime: float

    def __init__(self, rootSettlement):
        super().__init__()
        self._elementsList = []
        self.__maxListLength = 7
        self.__rootSettlement = rootSettlement

    def start(self):
        pass

    def update(self):
        pass

    def addElementToQueue(self, troopMovementElement: TroopMovementElement):
        if len(self._elementsList) < self.__maxListLength:
            self._elementsList.append(troopMovementElement)

    def _updateQueueContent(self, timePassed: float):
        elemsToRemove = []
        if len(self._elementsList) > 0:
            for elem in self._elementsList:
                elem.modifyRealTimeToFinish(elem.realTimeToFinish - timePassed)
                if elem.realTimeToFinish <= 0:
                    elemsToRemove.append(elem)
        for elem in elemsToRemove:
            self._elementsList.remove(elem)
            if not elem.isRetreating:
                # calculate the battle and add a come back element, if it was attacking movement:
                battle = Battle(elem)
                # TO-DO: generate the report
                self.__rootSettlement.getReports().addReport(ReportElement(
                    battleResult=battle.getBattleResult(),
                    attackSize=elem.attackSize,
                    attackingPlayerName=elem.attackingPlayer,
                    defendingPlayerName=elem.defendingPlayer,
                    attackingSettlementName="",
                    defendingSettlementName="",
                    attackingSettlementLocation=elem.attackingSettlementLocation,
                    defendingSettlementLocation=elem.defendingSettlementLocation,
                    timestampInSeconds=int(self.__currentTime),
                    initialAttackingArmyDict=battle.getInitialAttackingArmy(),
                    initialDefendingArmyDict=battle.getInitialDefendingArmy(),
                    attackingArmyLossesDict=battle.getAttackingLosses(),
                    defendingArmyLossesDict=battle.getDefendingLosses(),
                    buttonListener=self.reportButtonListener,
                    isFailedAttack=not battle.attackingArmyWon()
                ))
                # army comes back home - add retreating element
                if battle.attackingArmyWon():
                    self.addElementToQueue(TroopMovementElement(
                        elem.attackSize,
                        elem.fromEnemy,
                        elem.defendingSettlement,
                        elem.attackingSettlement,
                        int(elem.originalRealTimeToFinish),
                        elem.originalRealTimeToFinish,
                        attackingArmy=elem.attackingArmy,
                        defendingArmy=elem.defendingArmy,
                        isRetreating=True
                    ))
            else:
                self.__rootSettlement.addStationingUnitsFromDict(elem.attackingArmy)

    # overridden from MonoBehaviour
    def updateOnRealTime(self, realTime: float):
        super().updateOnRealTime(realTime)
        self.__currentTime = realTime

    # possibly add ReportsElement as an argument, and then pass this argument in reports_view
    def reportButtonListener(self, reportElement: ReportElement):
        pass

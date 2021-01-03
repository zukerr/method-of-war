# t = s/v
# example speed: 0.1 units per second
from mini_engine.game_machine.a_passing_time_aware_mono_behaviour import PassingTimeAwareMonoBehaviour
from method_of_war.ui.persistent_ui.troop_movements_view import TroopMovementElement
from typing import List
from method_of_war.core.attacks.battle import *


class TroopMovements(PassingTimeAwareMonoBehaviour):
    _elementsList: List[TroopMovementElement] = []
    __maxListLength: int
    __rootSettlement = None

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
                Battle(elem)
                # army comes back home - add retreating element
                self.addElementToQueue(TroopMovementElement(
                    elem.attackSize,
                    elem.fromEnemy,
                    elem.attackingSettlement,
                    elem.defendingSettlement,
                    int(elem.originalRealTimeToFinish),
                    elem.originalRealTimeToFinish,
                    attackingArmy=elem.attackingArmy,
                    defendingArmy=elem.defendingArmy,
                    isRetreating=True
                ))
            else:
                self.__rootSettlement.addStationingUnitsFromDict(elem.attackingArmy)

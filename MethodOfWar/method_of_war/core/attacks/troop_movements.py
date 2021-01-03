# t = s/v
# example speed: 0.1 units per second
from mini_engine.game_machine.a_passing_time_aware_mono_behaviour import PassingTimeAwareMonoBehaviour
from method_of_war.ui.persistent_ui.troop_movements_view import TroopMovementElement
from typing import List


class TroopMovements(PassingTimeAwareMonoBehaviour):
    _elementsList: List[TroopMovementElement] = []
    __maxListLength: int

    def __init__(self):
        super().__init__()
        self._elementsList = []
        self.__maxListLength = 7

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
            # calculate the battle and add a come back element
            # self.__settlement....

from mini_engine.game_machine.a_mono_behaviour import *
from abc import *


class Building(MonoBehaviour, ABC):
    _level: int

    def __init__(self, startingLevel: int):
        super().__init__()
        self._level = startingLevel

    @abstractmethod
    def levelUp(self):
        pass

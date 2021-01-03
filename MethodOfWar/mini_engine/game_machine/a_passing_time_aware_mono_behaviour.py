from mini_engine.game_machine.a_mono_behaviour import *
from abc import *


class PassingTimeAwareMonoBehaviour(MonoBehaviour, ABC):
    __firstUpdate: bool = False
    __oldTime: float

    @abstractmethod
    def _updateQueueContent(self, timePassed: float):
        pass

    def __updateQueue(self, realTime: float):
        if not self.__firstUpdate:
            self.__firstUpdate = True
        else:
            timePassed: float = realTime - self.__oldTime
            self._updateQueueContent(timePassed)
        self.__oldTime = realTime

    def updateOnRealTime(self, realTime: float):
        self.__updateQueue(realTime)

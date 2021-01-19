from method_of_war.ui import global_persistent_view_manager
from mini_engine.game_machine.a_mono_behaviour import *
from mini_engine.util.extensions import *


class GameTimer(MonoBehaviour):
    __timeSeconds: float

    def getTimeIntSeconds(self) -> int:
        return int(self.__timeSeconds)

    def __getTimeString(self) -> str:
        return getMinutesSecondsFromSeconds(self.getTimeIntSeconds())

    def start(self):
        self.__timeSeconds = 0

    def update(self):
        pass

    def updateOnRealTime(self, realTime: float):
        self.__timeSeconds = realTime
        global_persistent_view_manager.globalPersistentViewManager.getTopActionBar().updateTimerText(self.__getTimeString())

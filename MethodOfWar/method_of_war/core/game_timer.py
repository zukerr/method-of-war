from mini_engine.game_machine.a_mono_behaviour import *
from mini_engine.game_machine.game_machine_global import *
from mini_engine.util.extensions import *
from method_of_war.ui import global_persistent_view_manager
import time
from mini_engine.game_machine.game_machine_global import gameMachine


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

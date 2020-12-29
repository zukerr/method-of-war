from mini_engine.game_machine.a_mono_behaviour import *
from mini_engine.util.extensions import *


class Invoker(MonoBehaviour):
    __firstUpdate: bool = False
    __startTime: float
    __delay: float
    __currentDelay: float
    __functionToExecute = lambda: None

    def __init__(self, functionName, delay):
        super().__init__()
        self.__delay = delay
        self.__functionToExecute = functionName

    def start(self):
        pass

    def update(self):
        pass

    def updateOnRealTime(self, realTime: float):
        if not self.__firstUpdate:
            self.__firstUpdate = True
            self.__startTime = realTime
        else:
            self.__currentDelay = realTime - self.__startTime
            if self.__currentDelay >= self.__delay:
                self.setActive(False)
                self.__functionToExecute()

    def getTimeLeft(self) -> float:
        return self.__delay - self.__currentDelay

    def getReadableTimeLeft(self) -> str:
        return getMinutesSecondsFromSeconds(int(self.getTimeLeft()))


def invoke(functionName, time: float):
    Invoker(functionName, time)

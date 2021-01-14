from mini_engine.game_machine.game_machine_global import *
from abc import *
import pygame


class MonoBehaviour(Observer, ABC):
    __active = True

    def __init__(self):
        self.start()
        gameMachine.attachPattern(self)

    def setActive(self, value: bool):
        self.__active = value

    def isActive(self) -> bool:
        return self.__active

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def updateOnEvent(self, event: pygame.event):
        pass

    def updateOnRealTime(self, realTime: float):
        pass

    def lateUpdate(self):
        pass

    def updateOnEventPattern(self, event: pygame.event):
        if self.__active:
            self.updateOnEvent(event)

    def updatePattern(self, subject: Subject):
        if self.__active:
            self.update()

    def updateOnRealTimePattern(self, realTime: float):
        if self.__active:
            self.updateOnRealTime(realTime)

    def lateUpdatePattern(self, subject: Subject):
        if self.__active:
            self.lateUpdate()

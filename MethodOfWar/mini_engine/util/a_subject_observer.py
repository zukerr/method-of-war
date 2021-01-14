from __future__ import annotations
import pygame
from abc import *


class Subject(ABC):

    @abstractmethod
    def attachPattern(self, observer: Observer):
        # polacz obserwatora do podmiotu
        pass

    @abstractmethod
    def detachPattern(self, observer: Observer):
        # odlacz obserwatora
        pass

    @abstractmethod
    def notifyPattern(self):
        # powiadom wszystkich obserwatorow o zdarzeniu
        pass

    @abstractmethod
    def notifyOnEventPattern(self, event: pygame.event):
        pass

    @abstractmethod
    def notifyOnRealTimePattern(self, realTime: float):
        pass

    @abstractmethod
    def lateNotifyPattern(self):
        pass


class Observer(ABC):

    @abstractmethod
    def updatePattern(self, subject: Subject):
        # zaktualizuj obserwatora wzgledem podmiotu
        pass

    @abstractmethod
    def updateOnEventPattern(self, event: pygame.event):
        pass

    @abstractmethod
    def updateOnRealTimePattern(self, realTime: float):
        pass

    @abstractmethod
    def lateUpdatePattern(self, subject: Subject):
        pass

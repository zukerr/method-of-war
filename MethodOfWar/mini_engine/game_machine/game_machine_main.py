from mini_engine.util.a_subject_observer import *
from typing import List
import pygame


class GameMachine(Subject):
    __observers: List[Observer] = []

    def attachPattern(self, observer: Observer):
        self.__observers.append(observer)

    def detachPattern(self, observer: Observer):
        self.__observers.remove(observer)

    def notifyPattern(self):
        for observer in self.__observers:
            observer.updatePattern(self)

    def notifyOnEventPattern(self, event: pygame.event):
        for observer in self.__observers:
            observer.updateOnEventPattern(event)

    def notifyOnRealTimePattern(self, realTime: float):
        for observer in self.__observers:
            observer.updateOnRealTimePattern(realTime)

    def lateNotifyPattern(self):
        for observer in self.__observers:
            observer.lateUpdatePattern(self)

    def onTick(self):
        self.notifyPattern()

    def onEvent(self, event: pygame.event):
        self.notifyOnEventPattern(event)

    def onRealTime(self, realTime: float):
        self.notifyOnRealTimePattern(realTime)

    def onLateTick(self):
        self.lateNotifyPattern()

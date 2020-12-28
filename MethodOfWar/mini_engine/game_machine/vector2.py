from __future__ import annotations
import math


class Vector2:
    def __getX(self):
        return self.__x

    def __setX(self, value):
        self.__x = value

    def __getY(self):
        return self.__y

    def __setY(self, value):
        self.__y = value

    x: float = property(__getX, __setX)
    y: float = property(__getY, __setY)

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def distanceFrom(self, other: Vector2) -> float:
        return math.sqrt(math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2))

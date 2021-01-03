from abc import *
from method_of_war.core.buildings.resources_requirement_model import ResourcesRequirementModel


class Unit(ABC):
    __name: str
    __isMelee: bool = True
    __maxHp: float
    __currentHp: float
    __armor: float
    __attackDamage: float
    __lootCapacity: int
    __resourceRequirement: ResourcesRequirementModel
    __movementSpeedInUnitsPerSecond: float
    __isDead: bool = False

    def __init__(self, isMelee: bool, maxHp: float, armor: float, attackDamage: float, lootCapacity: int,
                 name: str, resourceRequirement: ResourcesRequirementModel, movementSpeedInUnitsPerSecond: float):
        self.__isMelee = isMelee
        self.__maxHp = maxHp
        self.__currentHp = self.__maxHp
        self.__armor = armor
        self.__attackDamage = attackDamage
        self.__lootCapacity = lootCapacity
        self.__name = name
        self.__resourceRequirement = resourceRequirement
        self.__movementSpeedInUnitsPerSecond = movementSpeedInUnitsPerSecond

    def getDamage(self, damageValue: float):
        damageValue -= self.__armor
        if damageValue < 0:
            damageValue = 0
        self.__currentHp -= damageValue
        if self.__currentHp < 0:
            self.__currentHp = 0
            self.__isDead = True

    def dealDamageToOther(self, target):
        if target is not None:
            target.getDamage(self.__attackDamage)

    def getResourceRequirement(self) -> ResourcesRequirementModel:
        return self.__resourceRequirement

    def getName(self) -> str:
        return self.__name

    def getMovementSpeed(self) -> float:
        return self.__movementSpeedInUnitsPerSecond

    def getIsMelee(self) -> bool:
        return self.__isMelee

    def getIsDead(self) -> bool:
        return self.__isDead

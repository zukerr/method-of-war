from mini_engine.game_machine.a_mono_behaviour import *
from abc import *
from method_of_war.core.buildings.resources_requirement_model import ResourcesRequirementModel
from typing import List


class Building(MonoBehaviour, ABC):
    _level: int
    _upgradeRequirementsList: List[ResourcesRequirementModel] = []
    _currentUpgradeRequirement: ResourcesRequirementModel
    _maxLevel: int
    _name: str
    isUpgrading: bool = False

    def __init__(self, startingLevel: int):
        super().__init__()
        self._level = startingLevel
        self.setupMaxLvl()
        self.setupName()
        self._upgradeRequirementsList = []
        self.setupUpgradeRequirements()
        self._currentUpgradeRequirement = self._upgradeRequirementsList[self._level - 1]

    @abstractmethod
    def levelUp(self):
        if self._level >= self._maxLevel:
            return
        self._level += 1
        self._currentUpgradeRequirement = self._upgradeRequirementsList[self._level - 1]

    @abstractmethod
    def setupMaxLvl(self):
        pass

    @abstractmethod
    def setupName(self):
        pass

    @abstractmethod
    def setupUpgradeRequirements(self):
        pass

    def getLevel(self) -> int:
        return self._level

    def getName(self) -> str:
        return self._name

    def getTitle(self) -> str:
        return self._name + " (Level " + str(self._level) + ")"

    def getCurrentUpgradeRequirement(self) -> ResourcesRequirementModel:
        return self._currentUpgradeRequirement

    def getNextUpgradeRequirement(self) -> ResourcesRequirementModel:
        return self._upgradeRequirementsList[self._level]

    def __getBtnTextFromLevel(self, level: int):
        if level == 0:
            return "--> Build"
        else:
            return "--> Level " + str(level + 1)

    def getButtonText(self) -> str:
        return self.__getBtnTextFromLevel(self._level)

    def getButtonTextWhileUpgrading(self) -> str:
        return self.__getBtnTextFromLevel(self._level + 1)

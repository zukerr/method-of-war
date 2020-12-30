from method_of_war.core.buildings.a_building import *
from method_of_war.ui import global_persistent_view_manager
from method_of_war.ui import global_gameplay_view_manager
from typing import List
from method_of_war.core.units.unit_models.unit_recruitment_model import UnitRecruitmentModel
from method_of_war.ui.gameplay_ui.building_views.city_hall.city_hall_available_buildings_list_view import AvailableBuildingElement


class Barracks(Building):
    __recruitTimeReductionFactorDict = {
        1: 1,
        2: 0.95,
        3: 0.9,
        4: 0.85,
        5: 0.79,
        6: 0.75,
        7: 0.7,
        8: 0.68,
        9: 0.66,
        10: 0.64,
        11: 0.62,
        12: 0.6,
        13: 0.58,
        14: 0.56,
        15: 0.54,
        16: 0.52,
        17: 0.5,
        18: 0.48,
        19: 0.46,
        20: 0.44
    }
    __queueMaxLength: int = 8
    __currentRecruitTimeReduction: float

    __recruitmentQueue: List[UnitRecruitmentModel] = []
    __firstUpdate: bool = False
    __oldTime: float

    __availableRecruits: List[AvailableBuildingElement]

    def levelUp(self):
        super().levelUp()
        self.__currentRecruitTimeReduction = self.__recruitTimeReductionFactorDict[self._level]

    def setupMaxLvl(self):
        self._maxLevel = 20

    def setupName(self):
        self._name = "Barracks"

    def setupUpgradeRequirements(self):
        for i in range(self._maxLevel):
            tempValue = (((i * i * i) + i + 16) * 2) - 5
            tempWood = tempValue - 10
            tempIron = tempValue + 17
            self._upgradeRequirementsList.append(ResourcesRequirementModel(tempWood, tempValue, tempIron, i + 8))

    def start(self):
        pass

    def update(self):
        pass

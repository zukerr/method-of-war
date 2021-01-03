from method_of_war.core.buildings.a_building import *
from typing import List
from method_of_war.core.units.unit_models.unit_recruitment_model import UnitRecruitmentModel
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.city_hall.city_hall_available_buildings_list_view import AvailableBuildingElement
from method_of_war.core.units.rogue import *
from method_of_war.ui import global_gameplay_view_manager
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.barracks.recruitment_queue_list_view import RecruitmentQueueElement
from mini_engine.util.extensions import *
from method_of_war.core.units.hunter import *
from method_of_war.core.units.rogue import *
from method_of_war.core.units.warrior import *
from method_of_war.core.units.paladin import *
from mini_engine.game_machine.a_passing_time_aware_mono_behaviour import PassingTimeAwareMonoBehaviour


class Barracks(Building, PassingTimeAwareMonoBehaviour):
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
    __settlement = None

    __recruitmentQueue: List[UnitRecruitmentModel] = []

    _availableRecruitsList: List[AvailableBuildingElement] = []

    def __init__(self, startingLevel: int, settlement):
        super().__init__(startingLevel)
        self.__recruitmentQueue = []
        self._availableRecruitsList = []
        self.__settlement = settlement
        self.setupAvailableUnits()

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

    def _getUiReadableQueue(self) -> List[RecruitmentQueueElement]:
        uiQueue = []
        for elem in self.__recruitmentQueue:
            uiQueue.append(elem.getRecruitmentQueueElement())
        return uiQueue

    # queue
    def addUnitToQueue(self, unit: Unit):
        if len(self.__recruitmentQueue) >= self.__queueMaxLength:
            return
        self.__recruitmentQueue.append(UnitRecruitmentModel(unit))

    # overriden from PassingTimeMonoBehaviour
    def _updateQueueContent(self, timePassed: float):
        elemsToRemove = []
        if len(self.__recruitmentQueue) > 0:
            elem = self.__recruitmentQueue[0]
            elem.getRecruitmentQueueElement().realTimeToFinish -= timePassed
            # elem.getRecruitmentQueueElement().timeToFinish = getMinutesSecondsFromSeconds(int(elem.getRecruitmentQueueElement().realTimeToFinish))
            elem.getRecruitmentQueueElement().updateTimeToFinish()
            if elem.getRecruitmentQueueElement().realTimeToFinish <= 0:
                elemsToRemove.append(elem)
        for elem in elemsToRemove:
            self.__recruitmentQueue.remove(elem)
            # actually add new unit to the settlement
            self.__settlement.addStationingUnit(elem.getUnit())

    # available units
    def setupAvailableUnits(self):
        availableUnits: List[Unit] = [Hunter(), Warrior(), Paladin(), Rogue()]
        for elem in availableUnits:
            self.__setupAvailableUnit(elem)

    def __setupAvailableUnit(self, unit: Unit):
        resourceRequirement = unit.getResourceRequirement()

        def onClick():
            if len(self.__recruitmentQueue) >= self.__queueMaxLength:
                return
            if self.__settlement.getWarehouse().requirementCanBeSatisfied(resourceRequirement):
                self.__settlement.getWarehouse().spendRequirement(resourceRequirement)
                self.addUnitToQueue(unit)

        self._availableRecruitsList.append(AvailableBuildingElement(unit.getName(),
                                                                    unit.getName(),
                                                                    resourceRequirement.woodValue,
                                                                    resourceRequirement.graniteValue,
                                                                    resourceRequirement.ironValue,
                                                                    resourceRequirement.timeInSeconds,
                                                                     "--> Recruit",
                                                                    isUnit=True,
                                                                    buttonFunction=onClick))

    def start(self):
        pass

    def update(self):
        pass

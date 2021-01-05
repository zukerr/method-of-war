from method_of_war.core.buildings.a_building import *
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.city_hall.city_hall_queue_list_view import BuildingQueueElement
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.city_hall.city_hall_available_buildings_list_view import AvailableBuildingElement
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.city_hall.city_hall_not_available_buildings_list_view import NotAvailableBuildingElement
from method_of_war.ui import global_gameplay_view_manager
from mini_engine.util.extensions import *
from mini_engine.game_machine.invoke import invoke
from mini_engine.game_machine.a_passing_time_aware_mono_behaviour import PassingTimeAwareMonoBehaviour


class CityHall(Building, PassingTimeAwareMonoBehaviour):
    __buildTimeReductionFactorDict = {
        1: 1,
        2: 0.95,
        3: 0.9,
        4: 0.85,
        5: 0.8,
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
    __maxQueueSize: int = 2
    __currentBuildTimeReduction: float
    __settlement = None

    _buildingQueue: List[BuildingQueueElement] = []

    _availableBuildingsList: List[AvailableBuildingElement] = []
    __notAvailableBuildingsList: List[NotAvailableBuildingElement] = []

    def __init__(self, startingLevel: int, settlement):
        super().__init__(startingLevel)
        self._buildingQueue = []
        self._availableBuildingsList = []
        self.__notAvailableBuildingsList = []
        self.__settlement = settlement
        self.setupAvailableBuildings()

    def levelUp(self):
        super().levelUp()
        self.__currentBuildTimeReduction = self.__buildTimeReductionFactorDict[self._level]

    def setupMaxLvl(self):
        self._maxLevel = 20

    def setupName(self):
        self._name = "City Hall"

    def setupUpgradeRequirements(self):
        for i in range(self._maxLevel):
            tempValue = (((i * i * i) + i + 11) * 2) - 5
            self._upgradeRequirementsList.append(ResourcesRequirementModel(tempValue + 3, tempValue + 10, tempValue - 2, i + 6))

    # queue
    def addUpgradeToQueue(self, building: Building):
        if len(self._buildingQueue) >= self.__maxQueueSize:
            return
        tempLevel = building.getLevel()
        tempReq = building.getCurrentUpgradeRequirement()
        if building.isUpgrading or (len(self._buildingQueue) > 0 and self._buildingQueue[0].buildingName == building.getName()):
            tempLevel += 1
            tempReq = building.getNextUpgradeRequirement()
        self._buildingQueue\
            .append(BuildingQueueElement(building.getName() + " (Level " + str(tempLevel + 1) + ")", tempReq.timeInSeconds,
                                         tempReq.timeInSeconds,
                                         building.getName()))
        building.isUpgrading = True
        # update available buildings
        self.setupAvailableBuildings()
        invoke(self._redrawAvailableBuildingsLive, 0.1)

    # overriden from PassingTimeAwareMonoBehaviour
    def _updateQueueContent(self, timePassed: float):
        elemsToRemove = []
        if len(self._buildingQueue) > 0:
            elem = self._buildingQueue[0]
            elem.realTimeToFinish -= timePassed
            elem.timeToFinish = getMinutesSecondsFromSeconds(int(elem.realTimeToFinish))
            if elem.realTimeToFinish <= 0:
                elemsToRemove.append(elem)
        for elem in elemsToRemove:
            self._buildingQueue.remove(elem)
            # actually upgrade proper building
            self.__settlement.getBuildingByName(elem.buildingName).levelUp()
            # redraw all early
            self.setupAvailableBuildings()
            self._redrawAvailableBuildingsLive()
            self.__settlement.getBuildingByName(elem.buildingName).isUpgrading = False
        # update available buildings view
        self.setupAvailableBuildings()

    def _redrawAvailableBuildingsLive(self):
        pass

    def __findAvailableBuildingByName(self, buildingName: str):
        for availBuilding in self._availableBuildingsList:
            if availBuilding.buildingName == buildingName:
                return availBuilding
        return None

    # available buildings
    def setupAvailableBuildings(self):
        # print("CITY_HALL: state of available buildings: ")
        buildingsList = self.__settlement.getBuildingsList()
        self._availableBuildingsList.clear()
        for building in buildingsList:
            self.__setupAvailableBuilding(building)

    def addLevelToAvailableBuildingElement(self, availBuildingElem: AvailableBuildingElement):
        correspondingBuilding = self.__settlement.getBuildingByName(availBuildingElem.buildingName)
        btnText = correspondingBuilding.getButtonTextWhileUpgrading()
        upgradeReq: ResourcesRequirementModel = correspondingBuilding.getUpgradeRequirementWithAddedLevel(1)
        availBuildingElem.buttonText = btnText
        availBuildingElem.buildingWoodReq = upgradeReq.woodValue
        availBuildingElem.buildingGraniteReq = upgradeReq.graniteValue
        availBuildingElem.buildingIronReq = upgradeReq.ironValue

    def __setupAvailableBuilding(self, building: Building):
        # handle case where there are buildings in queue, update info from existing buildings accordingly
        btnText = building.getButtonText()
        upgradeReq = building.getCurrentUpgradeRequirement()
        # one of the same in the queue
        if len(self._buildingQueue) == 1:
            if building.getName() == self._buildingQueue[0].buildingName:
                btnText = building.getButtonTextWhileUpgrading()
                upgradeReq = building.getUpgradeRequirementWithAddedLevel(1)
        # two of the same in the queue
        elif len(self._buildingQueue) == 2:
            if building.getName() == self._buildingQueue[0].buildingName == self._buildingQueue[1].buildingName:
                btnText = building.getButtonTextWithAddedLevel(2)
                upgradeReq = building.getUpgradeRequirementWithAddedLevel(2)
            else:
                if (building.getName() == self._buildingQueue[0].buildingName) or (building.getName() == self._buildingQueue[1].buildingName):
                    btnText = building.getButtonTextWhileUpgrading()
                    upgradeReq = building.getUpgradeRequirementWithAddedLevel(1)

        def onClick():
            if len(self._buildingQueue) >= self.__maxQueueSize:
                return
            if building.availableForLevelUp():
                if self.__settlement.getWarehouse().requirementCanBeSatisfied(upgradeReq):
                    self.__settlement.getWarehouse().spendRequirement(upgradeReq)
                    self.addUpgradeToQueue(building)

        self._availableBuildingsList.append(AvailableBuildingElement(building.getName(),
                                                                     building.getTitle(),
                                                                     upgradeReq.woodValue,
                                                                     upgradeReq.graniteValue,
                                                                     upgradeReq.ironValue,
                                                                     upgradeReq.timeInSeconds,
                                                                     btnText,
                                                                     buttonFunction=onClick))
        # print("CITY_HALL: added new building for: " + self.__settlement.getOwnerName())

    def start(self):
        pass

    def update(self):
        pass

from method_of_war.core.attacks.troop_movements import TroopMovements
from method_of_war.core.buildings.barracks import Barracks
from method_of_war.core.reports.reports import Reports
from method_of_war.core.units.unit_models.a_unit import Unit
from mini_engine.game_machine.a_mono_behaviour import *
from method_of_war.core.buildings.warehouse import *
from method_of_war.core.buildings.production_building import *
from method_of_war.enums.resource_type import ResourceType
from method_of_war.core.buildings.city_hall import *
from method_of_war.core.buildings.a_building import Building
from method_of_war.ui import global_persistent_view_manager
from method_of_war.core.units.unit_models.unit_factory import MakeUnit


class Settlement(MonoBehaviour):
    _cityHall: CityHall
    _warehouse: Warehouse
    _lumberMill: ProductionBuilding
    _quarry: ProductionBuilding
    _mine: ProductionBuilding
    _barracks: Barracks

    _troopMovements: TroopMovements
    _reports: Reports

    _buildingsList: List[Building] = []
    _stationingUnitsDict = {
        "Warrior": 0,
        "Paladin": 0,
        "Rogue": 0,
        "Hunter": 0,
        "Mage": 0,
        "Priest": 0,
        "Warlock": 0,
        "Shaman": 0,
        "Death Knight": 0,
        "Druid": 0,
        "Monk": 0
    }
    __stationingUnitsList: List[Unit] = []

    __ownerName: str = ""
    __location: (int, int) = (-1, -1)

    def __init__(self, ownerName: str, location: (int, int)):
        super().__init__()
        self.__ownerName = ownerName
        self.__location = location
        self.__stationingUnitsList = []
        self._buildingsList = []
        self._stationingUnitsDict = {
            "Warrior": 0,
            "Paladin": 0,
            "Rogue": 0,
            "Hunter": 0,
            "Mage": 0,
            "Priest": 0,
            "Warlock": 0,
            "Shaman": 0,
            "Death Knight": 0,
            "Druid": 0,
            "Monk": 0
        }

    def start(self):
        pass

    def update(self):
        # print("updating the village...")
        pass

    def getWarehouse(self) -> Warehouse:
        return self._warehouse

    def getLumberMill(self) -> ProductionBuilding:
        return self._lumberMill

    def getQuarry(self) -> ProductionBuilding:
        return self._quarry

    def getMine(self) -> ProductionBuilding:
        return self._mine

    def getBuildingsList(self) -> List[Building]:
        return self._buildingsList

    def getBuildingByName(self, name: str):
        for building in self._buildingsList:
            if building.getName() == name:
                return building
        return None

    def addStationingUnit(self, unit: Unit, quantity: int = 1):
        if unit is not None:
            for i in range(quantity):
                self.__stationingUnitsList.append(unit)
            self._stationingUnitsDict[unit.getName()] += quantity

    def addStationingUnitsFromDict(self, inputUnitDict: dict):
        keyList = list(self._stationingUnitsDict.keys())
        for key in keyList:
            self.addStationingUnit(MakeUnit(key), inputUnitDict[key])

    def getStationingUnitsDict(self) -> dict:
        return self._stationingUnitsDict

    def removeStationingUnit(self, unitName: str, quantity: int = 1):
        if quantity > self._stationingUnitsDict[unitName]:
            return
        self._stationingUnitsDict[unitName] -= quantity
        print("stationing units in " + self.__ownerName + ": ")
        print(self._stationingUnitsDict)
        print(self.__stationingUnitsList)
        for i in range(quantity):
            self.__stationingUnitsList.remove(self.findStationingUnitInListByName(unitName))

    def findStationingUnitInListByName(self, unitName: str):
        for unit in self.__stationingUnitsList:
            if unit.getName() == unitName:
                return unit
        return None

    def getOwnerName(self) -> str:
        return self.__ownerName

    def getLocation(self) -> (int, int):
        return self.__location

    def getLocationStr(self) -> str:
        return "(" + str(self.__location[0]) + ", " + str(self.__location[1]) + ")"

    def getTroopMovements(self) -> TroopMovements:
        return self._troopMovements

    def getReports(self) -> Reports:
        return self._reports

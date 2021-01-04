from method_of_war.core.player_core.player_reports import PlayerReports
from method_of_war.core.player_core.player_troop_movements import PlayerTroopMovements
from method_of_war.core.settlement import *
from method_of_war.core.player_core.player_city_hall import *
from method_of_war.core.player_core.player_barracks import *
from method_of_war.core.player_core.player_production_building import *
from method_of_war.core.player_core.player_warehouse import *


class PlayerSettlement(Settlement):

    def __init__(self, ownerName: str, location: (int, int)):
        super().__init__(ownerName, location)
        global_persistent_view_manager.globalPersistentViewManager.getUnits().updateUnits(self._stationingUnitsDict)

        self._cityHall = PlayerCityHall(1, self)
        self._buildingsList.append(self._cityHall)

        self._warehouse = PlayerWarehouse(1, 0, 0, 0)
        self._buildingsList.append(self._warehouse)

        self._lumberMill = PlayerProductionBuilding(1, ResourceType.WOOD, self._warehouse)
        self._buildingsList.append(self._lumberMill)

        self._quarry = PlayerProductionBuilding(1, ResourceType.GRANITE, self._warehouse)
        self._buildingsList.append(self._quarry)

        self._mine = PlayerProductionBuilding(1, ResourceType.IRON, self._warehouse)
        self._buildingsList.append(self._mine)

        self._barracks = PlayerBarracks(1, self)
        self._buildingsList.append(self._barracks)

        self._cityHall.setupAvailableBuildings()

        self._troopMovements = PlayerTroopMovements(self)
        self._reports = PlayerReports()

    def addStationingUnit(self, unit: Unit, quantity: int = 1):
        super().addStationingUnit(unit, quantity)
        global_persistent_view_manager.globalPersistentViewManager.getUnits().updateUnits(self._stationingUnitsDict)

    def removeStationingUnit(self, unitName: str, quantity: int = 1):
        super().removeStationingUnit(unitName, quantity)
        global_persistent_view_manager.globalPersistentViewManager.getUnits().updateUnits(self._stationingUnitsDict)

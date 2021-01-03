from method_of_war.core.settlement import *
from method_of_war.core.player_core.player_city_hall import *
from method_of_war.core.player_core.player_barracks import *
from method_of_war.core.player_core.player_production_building import *
from method_of_war.core.player_core.player_warehouse import *


class PlayerSettlement(Settlement):

    def start(self):
        global_persistent_view_manager.globalPersistentViewManager.getUnits().updateUnits(self._stationingUnitsDict)
        self._buildingsList = []

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

    def addStationingUnit(self, unit: Unit, quantity: int = 1):
        super().addStationingUnit(unit, quantity)
        global_persistent_view_manager.globalPersistentViewManager.getUnits().updateUnits(self._stationingUnitsDict)

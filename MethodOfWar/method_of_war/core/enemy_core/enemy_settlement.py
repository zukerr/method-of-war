from method_of_war.core.buildings.barracks import Barracks
from method_of_war.core.units.unit_models.a_unit import Unit
from mini_engine.game_machine.a_mono_behaviour import *
from method_of_war.core.buildings.warehouse import *
from method_of_war.core.buildings.production_building import *
from method_of_war.enums.resource_type import ResourceType
from method_of_war.core.buildings.city_hall import *
from method_of_war.core.buildings.a_building import Building
from method_of_war.core.settlement import *


class EnemySettlement(Settlement):

    def __init__(self, ownerName: str, location: (int, int)):
        super().__init__(ownerName, location)

        self._cityHall = CityHall(1, self)
        self._buildingsList.append(self._cityHall)

        self._warehouse = Warehouse(1, 0, 0, 0)
        self._buildingsList.append(self._warehouse)

        self._lumberMill = ProductionBuilding(1, ResourceType.WOOD, self._warehouse)
        self._buildingsList.append(self._lumberMill)

        self._quarry = ProductionBuilding(1, ResourceType.GRANITE, self._warehouse)
        self._buildingsList.append(self._quarry)

        self._mine = ProductionBuilding(1, ResourceType.IRON, self._warehouse)
        self._buildingsList.append(self._mine)

        self._barracks = Barracks(1, self)
        self._buildingsList.append(self._barracks)

        self._cityHall.setupAvailableBuildings()

        self._troopMovements = TroopMovements(self)

from method_of_war.core.enemy_core.enemy_barracks import *
from method_of_war.core.enemy_core.enemy_city_hall import *
from method_of_war.core.settlement import *


class EnemySettlement(Settlement):

    def __init__(self, ownerName: str, location: (int, int)):
        super().__init__(ownerName, location)

        self._cityHall = EnemyCityHall(1, self)
        self._buildingsList.append(self._cityHall)

        self._warehouse = Warehouse(1, 0, 0, 0)
        self._buildingsList.append(self._warehouse)

        self._lumberMill = ProductionBuilding(1, ResourceType.WOOD, self._warehouse)
        self._buildingsList.append(self._lumberMill)

        self._quarry = ProductionBuilding(1, ResourceType.GRANITE, self._warehouse)
        self._buildingsList.append(self._quarry)

        self._mine = ProductionBuilding(1, ResourceType.IRON, self._warehouse)
        self._buildingsList.append(self._mine)

        self._barracks = EnemyBarracks(1, self)
        self._buildingsList.append(self._barracks)

        self._cityHall.setupAvailableBuildings()

        self._troopMovements = TroopMovements(self)
        self._reports = Reports()

    def getCityHall(self):
        return self._cityHall

    def getBarracks(self):
        return self._barracks

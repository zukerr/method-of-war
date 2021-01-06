from method_of_war.core.buildings.city_hall import CityHall


class EnemyCityHall(CityHall):
    def getQueueCount(self) -> int:
        return len(self._buildingQueue)

    def ghostClickLevelUpBuilding(self, buildingName: str):
        availBuilding = self._findAvailableBuildingByName(buildingName)
        availBuilding.buttonFunction()

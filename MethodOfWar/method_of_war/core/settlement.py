from mini_engine.game_machine.a_mono_behaviour import *
from method_of_war.core.buildings.warehouse import *
from method_of_war.core.buildings.production_building import *
from method_of_war.enums.resource_type import ResourceType
from method_of_war.core.buildings.city_hall import *
from method_of_war.core.buildings.a_building import Building


class Settlement(MonoBehaviour):
    __cityHall: CityHall
    __warehouse: Warehouse
    __lumberMill: ProductionBuilding
    __quarry: ProductionBuilding
    __mine: ProductionBuilding

    __buildingsList: List[Building] = []

    def start(self):
        self.__cityHall = CityHall(1, self)
        self.__buildingsList.append(self.__cityHall)

        self.__warehouse = Warehouse(1, 0, 0, 0)
        self.__buildingsList.append(self.__warehouse)

        self.__lumberMill = ProductionBuilding(1, ResourceType.WOOD, self.__warehouse)
        self.__buildingsList.append(self.__lumberMill)

        self.__quarry = ProductionBuilding(1, ResourceType.GRANITE, self.__warehouse)
        self.__buildingsList.append(self.__quarry)

        self.__mine = ProductionBuilding(1, ResourceType.IRON, self.__warehouse)
        self.__buildingsList.append(self.__mine)

        self.__cityHall.setupAvailableBuildings()

    def update(self):
        # print("updating the village...")
        pass

    def getWarehouse(self) -> Warehouse:
        return self.__warehouse

    def getLumberMill(self) -> ProductionBuilding:
        return self.__lumberMill

    def getQuarry(self) -> ProductionBuilding:
        return self.__quarry

    def getMine(self) -> ProductionBuilding:
        return self.__mine

    def getBuildingsList(self) -> List[Building]:
        return self.__buildingsList

    def getBuildingByName(self, name: str):
        for building in self.__buildingsList:
            if building.getName() == name:
                return building
        return None

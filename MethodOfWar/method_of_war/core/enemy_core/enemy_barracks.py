from method_of_war.core.buildings.barracks import Barracks
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.city_hall.city_hall_available_buildings_list_view import AvailableBuildingElement


class EnemyBarracks(Barracks):
    def findAvailableUnit(self, unitName: str):
        for elem in self._availableRecruitsList:
            if elem.buildingName == unitName:
                return elem
        return None

    def ghostClickRecruitUnit(self, unitName: str):
        targetUnit = self.findAvailableUnit(unitName)
        targetUnit.buttonFunction()

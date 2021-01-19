from method_of_war.core.buildings.barracks import Barracks


class EnemyBarracks(Barracks):
    def findAvailableUnit(self, unitName: str):
        for elem in self._availableRecruitsList:
            if elem.buildingName == unitName:
                return elem
        return None

    def ghostClickRecruitUnit(self, unitName: str):
        targetUnit = self.findAvailableUnit(unitName)
        targetUnit.buttonFunction()

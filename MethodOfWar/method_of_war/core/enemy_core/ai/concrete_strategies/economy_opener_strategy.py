from method_of_war.core.enemy_core.ai.a_opener_strategy import OpenerStrategy
from method_of_war.core.enemy_core.enemy_settlement import EnemySettlement
from method_of_war.core.player_core.player_settlement import PlayerSettlement
from method_of_war.core.enemy_core.enemy_city_hall import EnemyCityHall
from method_of_war.core.buildings.resources_requirement_model import ResourcesRequirementModel
from method_of_war.core.enemy_core.enemy_barracks import EnemyBarracks


class EconomyOpenerStrategy(OpenerStrategy):
    __nextEcoLevel: int = 2
    __targetEcoLevel: int = 5

    __targetPaladinCount: int = 3

    __setupComplete: bool = False

    def executeOpener(self, realTime: float, playerSettlement: PlayerSettlement, mySettlement: EnemySettlement,
                      actionIntervalInSeconds: int = 0):
        # build eco
        if actionIntervalInSeconds != 0:
            if not int(realTime) % actionIntervalInSeconds == 0:
                return
        if not self.__firstStepComplete():
            myCityHall: EnemyCityHall = mySettlement.getCityHall()
            if myCityHall.getQueueCount() < 2:
                if mySettlement.getMine().getLevel() < self.__nextEcoLevel:
                    myCityHall.ghostClickLevelUpBuilding("Mine")
            if myCityHall.getQueueCount() < 2:
                if mySettlement.getQuarry().getLevel() < self.__nextEcoLevel:
                    myCityHall.ghostClickLevelUpBuilding("Quarry")
            if myCityHall.getQueueCount() < 2:
                if mySettlement.getLumberMill().getLevel() < self.__nextEcoLevel:
                    myCityHall.ghostClickLevelUpBuilding("Lumber Mill")
            if mySettlement.getLumberMill().getLevel() == self.__nextEcoLevel \
                    and mySettlement.getQuarry().getLevel() == self.__nextEcoLevel \
                    and mySettlement.getMine().getLevel() == self.__nextEcoLevel:
                self.__nextEcoLevel += 1

        # recruit base of defense
        if self.__firstStepComplete():
            if mySettlement.getStationingUnitsDict()["Paladin"] < 3:
                myBarracks: EnemyBarracks = mySettlement.getBarracks()
                myBarracks.ghostClickRecruitUnit("Paladin")
            else:
                self.__setupComplete = True

    def openerDone(self) -> bool:
        return self.__setupComplete

    def __firstStepComplete(self) -> bool:
        return self.__nextEcoLevel == (self.__targetEcoLevel + 1)

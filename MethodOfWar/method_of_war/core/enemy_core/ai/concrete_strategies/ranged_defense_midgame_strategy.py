from method_of_war.core.enemy_core.ai.a_midgame_strategy import MidgameStrategy
from method_of_war.core.enemy_core.enemy_barracks import EnemyBarracks
from method_of_war.core.enemy_core.enemy_settlement import EnemySettlement
from method_of_war.core.player_core.player_settlement import PlayerSettlement


class RangedDefenseMidgameStrategy(MidgameStrategy):
    def executeMidgameStrategy(self, realTime: float, playerSettlement: PlayerSettlement, mySettlement: EnemySettlement,
                               actionIntervalInSeconds: int = 0):
        myBarracks: EnemyBarracks = mySettlement.getBarracks()
        if mySettlement.getStationingUnitsDict()["Paladin"] < 3:
            myBarracks.ghostClickRecruitUnit("Paladin")
        else:
            myBarracks.ghostClickRecruitUnit("Hunter")

    def midgameIsOver(self) -> bool:
        return False

from method_of_war.core.attacks.send_troops import SendTroops
from method_of_war.core.enemy_core.ai.a_midgame_strategy import MidgameStrategy
from method_of_war.core.enemy_core.enemy_settlement import EnemySettlement
from method_of_war.core.player_core.player_settlement import PlayerSettlement
from method_of_war.core.enemy_core.enemy_city_hall import EnemyCityHall
from method_of_war.core.buildings.resources_requirement_model import ResourcesRequirementModel
from method_of_war.core.enemy_core.enemy_barracks import EnemyBarracks


class RogueAggroMidgameStrategy(MidgameStrategy):
    def executeMidgameStrategy(self, realTime: float, playerSettlement: PlayerSettlement, mySettlement: EnemySettlement,
                               actionIntervalInSeconds: int = 0):
        myBarracks: EnemyBarracks = mySettlement.getBarracks()
        myBarracks.ghostClickRecruitUnit("Rogue")

        if mySettlement.getStationingUnitsDict()["Rogue"] >= 5:
            attack = SendTroops(mySettlement, playerSettlement)
            attack.addCurrentUnit("Rogue", 5)
            attack.sendAttack()

    def midgameIsOver(self) -> bool:
        return False

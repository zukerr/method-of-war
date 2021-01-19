from method_of_war.core.attacks.send_troops import SendTroops
from method_of_war.core.enemy_core.ai.a_opener_strategy import OpenerStrategy
from method_of_war.core.enemy_core.enemy_barracks import EnemyBarracks
from method_of_war.core.enemy_core.enemy_settlement import EnemySettlement
from method_of_war.core.player_core.player_settlement import PlayerSettlement


class HyperAggroOpenerStrategy(OpenerStrategy):

    def executeOpener(self, realTime: float, playerSettlement: PlayerSettlement, mySettlement: EnemySettlement,
                      actionIntervalInSeconds: int = 0):
        # recruit rogues
        myBarracks: EnemyBarracks = mySettlement.getBarracks()
        myBarracks.ghostClickRecruitUnit("Rogue")

        if mySettlement.getStationingUnitsDict()["Rogue"] > 0:
            attack = SendTroops(mySettlement, playerSettlement)
            attack.addCurrentUnit("Rogue", mySettlement.getStationingUnitsDict()["Rogue"])
            attack.sendAttack()

    def openerDone(self) -> bool:
        return False

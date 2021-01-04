from method_of_war.core.levels.a_game_level import GameLevel
from method_of_war.core.player_core.player_settlement import PlayerSettlement
from method_of_war.core.units.warrior import Warrior
from method_of_war.enums.map_node_type import NodeType
from method_of_war.ui import global_gameplay_view_manager
from method_of_war.core.settlement import Settlement
from method_of_war.core.enemy_core.enemy_settlement import *


class GameLevel1(GameLevel):
    def _setupSettlements(self):
        self._playerSettlement = PlayerSettlement("Player", (1, 2))
        self._enemySettlements.append(EnemySettlement("Thrall", (3, 1)))
        # add units to enemy settlement to test combat
        self._enemySettlements[0].addStationingUnit(Warrior(), 50)
        print("Players units:")
        print(self._playerSettlement.getStationingUnitsDict())
        print("Enemy units:")
        print(self._enemySettlements[0].getStationingUnitsDict())

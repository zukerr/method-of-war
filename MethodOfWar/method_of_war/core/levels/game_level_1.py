from method_of_war.core.enemy_core.ai.concrete_strategies.hyper_aggro_opener_strategy import HyperAggroOpenerStrategy
from method_of_war.core.levels.a_game_level import GameLevel
from method_of_war.core.player_core.player_settlement import PlayerSettlement
from method_of_war.core.enemy_core.enemy_settlement import *
from method_of_war.core.levels import global_level
from method_of_war.core.enemy_core.ai.base_ai_context import BaseAiContext
from method_of_war.core.enemy_core.ai.concrete_strategies.economy_opener_strategy import EconomyOpenerStrategy
from method_of_war.core.enemy_core.ai.concrete_strategies.ranged_defense_midgame_strategy import RangedDefenseMidgameStrategy
from method_of_war.core.enemy_core.ai.concrete_strategies.rogue_aggro_midgame_strategy import RogueAggroMidgameStrategy

class GameLevel1(GameLevel):
    def _setupSettlements(self):
        self._playerSettlement = PlayerSettlement("Player", (1, 2))
        global_level.globalSettlementsList.append(self._playerSettlement)
        self._enemySettlements.append(EnemySettlement("Thrall", (3, 1)))
        global_level.globalSettlementsList.append(self._enemySettlements[0])

        # ai elements
        # add units to enemy settlement to test combat
        # self._enemySettlements[0].addStationingUnit(Warrior(), 20)
        # print("Players units:")
        # print(self._playerSettlement.getStationingUnitsDict())
        # print("Enemy units:")
        # print(self._enemySettlements[0].getStationingUnitsDict())
        # enemyAttack1 = SendTroops(self._enemySettlements[0], self._playerSettlement)
        # enemyAttack1.addCurrentUnit("Warrior", 10)
        # invoke(enemyAttack1.sendAttack, 10)

        aiEnemy0 = BaseAiContext(self._playerSettlement, self._enemySettlements[0],
                                 HyperAggroOpenerStrategy(), RogueAggroMidgameStrategy())
        self._enemyAiList.append(aiEnemy0)

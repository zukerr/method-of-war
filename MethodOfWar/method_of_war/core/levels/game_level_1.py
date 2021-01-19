from method_of_war.core.enemy_core.ai.base_ai_context import BaseAiContext
from method_of_war.core.enemy_core.ai.concrete_strategies.hyper_aggro_opener_strategy import HyperAggroOpenerStrategy
from method_of_war.core.enemy_core.ai.concrete_strategies.rogue_aggro_midgame_strategy import RogueAggroMidgameStrategy
from method_of_war.core.enemy_core.enemy_settlement import *
from method_of_war.core.levels import global_level
from method_of_war.core.levels.a_game_level import GameLevel
from method_of_war.core.player_core.player_settlement import PlayerSettlement


class GameLevel1(GameLevel):
    def _setupSettlements(self):
        self._playerSettlement = PlayerSettlement("Player", (1, 2))
        global_level.globalSettlementsList.append(self._playerSettlement)
        self._enemySettlements.append(EnemySettlement("Thrall", (3, 1)))
        global_level.globalSettlementsList.append(self._enemySettlements[0])

        aiEnemy0 = BaseAiContext(self._playerSettlement, self._enemySettlements[0],
                                 HyperAggroOpenerStrategy(), RogueAggroMidgameStrategy())
        self._enemyAiList.append(aiEnemy0)

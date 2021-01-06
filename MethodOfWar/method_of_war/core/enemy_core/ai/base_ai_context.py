from method_of_war.core.enemy_core.ai.a_midgame_strategy import MidgameStrategy
from method_of_war.core.enemy_core.enemy_settlement import EnemySettlement
from method_of_war.core.player_core.player_settlement import PlayerSettlement
from mini_engine.game_machine.a_mono_behaviour import MonoBehaviour
from abc import ABC
from method_of_war.core.enemy_core.ai.a_opener_strategy import OpenerStrategy


class BaseAiContext(MonoBehaviour):
    __mySettlement: EnemySettlement
    __playerSettlement: PlayerSettlement

    __openerStrategy: OpenerStrategy
    __midgameStrategy: MidgameStrategy

    def __init__(self, playerSettlement: PlayerSettlement, mySettlement: EnemySettlement,
                 openerStrategy: OpenerStrategy,
                 midgameStrategy: MidgameStrategy):
        super().__init__()
        self.__mySettlement = mySettlement
        self.__playerSettlement = playerSettlement
        self.__openerStrategy = openerStrategy
        self.__midgameStrategy = midgameStrategy

    def start(self):
        pass

    def update(self):
        pass

    def updateOnRealTime(self, realTime: float):
        if not self.__openerStrategy.openerDone():
            self.__openerStrategy.executeOpener(realTime, self.__playerSettlement, self.__mySettlement, 3)
        else:
            if not self.__midgameStrategy.midgameIsOver():
                self.__midgameStrategy.executeMidgameStrategy(realTime, self.__playerSettlement, self.__mySettlement, 3)

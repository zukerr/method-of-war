from abc import *
from method_of_war.core.enemy_core.enemy_settlement import EnemySettlement
from method_of_war.core.player_core.player_settlement import PlayerSettlement


class OpenerStrategy(ABC):
    @abstractmethod
    def executeOpener(self, realTime: float, playerSettlement: PlayerSettlement, mySettlement: EnemySettlement,
                      actionIntervalInSeconds: int = 0):
        pass

    @abstractmethod
    def openerDone(self) -> bool:
        pass

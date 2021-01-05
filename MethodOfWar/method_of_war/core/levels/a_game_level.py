from abc import *
from method_of_war.core.player_core.player_send_troops import PlayerSendTroops
from method_of_war.enums.gameplay_view_type import GameplayViewType
from method_of_war.enums.map_node_type import NodeType
from method_of_war.ui import global_gameplay_view_manager
from method_of_war.core.settlement import *
from method_of_war.core.attacks import global_battles


class GameLevel(ABC):
    _playerSettlement: Settlement
    _enemySettlements: List[Settlement] = []

    def setupGameLevel(self):
        global_battles.globalBattleList = []
        self._enemySettlements = []
        self._setupSettlements()
        self._setupMap()

    def _setupMap(self):
        # setup player settlement node based on player settlement object
        global_gameplay_view_manager\
            .globalGameplayViewManager\
            .getMapView()\
            .setNode(self._playerSettlement.getLocation()[0],
                     self._playerSettlement.getLocation()[1],
                     NodeType.FRIENDLY,
                     False,
                     nodeButtonListener=lambda: global_gameplay_view_manager
                     .globalGameplayViewManager
                     .switchGameplayView(GameplayViewType.OVERVIEW))

        # setup enemy settlement nodes based on enemy settlement objects
        for elem in self._enemySettlements:
            global_gameplay_view_manager\
                .globalGameplayViewManager\
                .getMapView()\
                .setNode(elem.getLocation()[0],
                         elem.getLocation()[1],
                         NodeType.ENEMY,
                         False,
                         nodeButtonListener=lambda: PlayerSendTroops(self._playerSettlement, elem))

    @abstractmethod
    def _setupSettlements(self):
        pass

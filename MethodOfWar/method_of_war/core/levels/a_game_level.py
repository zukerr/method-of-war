from method_of_war.core.attacks import global_battles
from method_of_war.core.enemy_core.ai.base_ai_context import BaseAiContext
from method_of_war.core.enemy_core.enemy_settlement import EnemySettlement
from method_of_war.core.levels.game_result_control import GameResultControl
from method_of_war.core.player_core.player_send_troops import PlayerSendTroops
from method_of_war.core.player_core.player_settlement import PlayerSettlement
from method_of_war.core.settlement import *
from method_of_war.enums.gameplay_view_type import GameplayViewType
from method_of_war.enums.map_node_type import NodeType
from method_of_war.ui import global_gameplay_view_manager


class GameLevel(ABC):
    _playerSettlement: PlayerSettlement
    _enemySettlements: List[EnemySettlement] = []
    _enemyAiList: List[BaseAiContext]

    _gameResultControl: GameResultControl

    def setupGameLevel(self):
        global_battles.globalBattleList = []
        self._enemyAiList = []
        self._enemySettlements = []
        self._setupSettlements()
        self._setupMap()
        self._gameResultControl = GameResultControl(self._playerSettlement, self._enemySettlements, self.endLevel)

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
        self._playerSettlement.getSettlementDestruction().updateMapUi()

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
            elem.getSettlementDestruction().updateMapUi()

    @abstractmethod
    def _setupSettlements(self):
        pass

    def endLevel(self):
        for elem in self._enemyAiList:
            elem.setActive(False)

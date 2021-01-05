from method_of_war.core.attacks.send_troops import *
from method_of_war.ui import global_gameplay_view_manager
from method_of_war.enums.gameplay_view_type import GameplayViewType


class PlayerSendTroops(SendTroops):
    def __init__(self, fromSettlement, toSettlement):
        super().__init__(fromSettlement, toSettlement)
        global_gameplay_view_manager.globalGameplayViewManager.getSendTroopsView().updateTargetLocation(self._targetString)
        global_gameplay_view_manager.globalGameplayViewManager.getSendTroopsView().updateOwnerName(self._targetOwnerName)
        global_gameplay_view_manager.globalGameplayViewManager.getSendTroopsView().updateResetAllListener(self._resetAll)
        global_gameplay_view_manager.globalGameplayViewManager.getSendTroopsView().updateSendAttackListener(self.sendAttack)
        self.__drawView()

    def _setupElementList(self):
        super()._setupElementList()
        global_gameplay_view_manager.globalGameplayViewManager.getSendTroopsView().updateAvailableUnits(self._elementList)
        self.__drawView()

    def __drawView(self):
        global_gameplay_view_manager.globalGameplayViewManager.preClickBuildingView()
        global_gameplay_view_manager.globalGameplayViewManager.getSendTroopsView().disableView()
        global_gameplay_view_manager.globalGameplayViewManager.getSendTroopsView().drawView()
        global_gameplay_view_manager.globalGameplayViewManager.postClickBuildingView(
            global_gameplay_view_manager.globalGameplayViewManager.getSendTroopsView(),
            GameplayViewType.SEND_TROOPS
        )

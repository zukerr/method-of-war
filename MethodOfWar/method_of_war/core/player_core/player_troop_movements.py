from method_of_war.core.attacks.troop_movements import TroopMovements
from method_of_war.enums.gameplay_view_type import GameplayViewType
from method_of_war.ui import global_persistent_view_manager
from method_of_war.ui import global_gameplay_view_manager
from method_of_war.ui.gameplay_ui.reports.reports_list_view import ReportElement
from method_of_war.ui.persistent_ui.troop_movements_view import TroopMovementElement


class PlayerTroopMovements(TroopMovements):
    def addElementToQueue(self, troopMovementElement: TroopMovementElement):
        super().addElementToQueue(troopMovementElement)
        global_persistent_view_manager\
            .globalPersistentViewManager\
            .getTroopMovements()\
            .updateElementsList(self._elementsList)

    def _updateQueueContent(self, timePassed: float):
        super()._updateQueueContent(timePassed)
        global_persistent_view_manager.globalPersistentViewManager.getTroopMovements().updateElementsList(self._elementsList)
        global_persistent_view_manager.globalPersistentViewManager.getTroopMovements().drawView()

    # possibly add ReportsElement as an argument, and then pass this argument in reports_view
    def reportButtonListener(self, reportElement: ReportElement):
        print("Clicked a report from player_troop_movements")
        global_gameplay_view_manager.globalGameplayViewManager.preClickBuildingView()
        global_gameplay_view_manager.globalGameplayViewManager.getReportDetailsView().updateData(reportElement)
        global_gameplay_view_manager.globalGameplayViewManager.getReportDetailsView().drawView()
        global_gameplay_view_manager\
            .globalGameplayViewManager\
            .postClickBuildingView(global_gameplay_view_manager
                                   .globalGameplayViewManager
                                   .getReportDetailsView(),
                                   GameplayViewType.REPORT_DETAILS)

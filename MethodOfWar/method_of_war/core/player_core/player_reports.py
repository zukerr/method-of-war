from method_of_war.core.reports.reports import Reports
from method_of_war.ui import global_gameplay_view_manager
from method_of_war.ui.gameplay_ui.reports.reports_view import ReportElement


class PlayerReports(Reports):
    def __init__(self):
        super().__init__()
        global_gameplay_view_manager.globalGameplayViewManager.getReportsView().updateElementsList(self._elementList)

    def addReport(self, reportElement: ReportElement):
        super().addReport(reportElement)
        global_gameplay_view_manager.globalGameplayViewManager.getReportsView().updateElementsList(self._elementList)
        if global_gameplay_view_manager.globalGameplayViewManager.isReportsViewActive():
            global_gameplay_view_manager.globalGameplayViewManager.getReportsView().disableView()
            global_gameplay_view_manager.globalGameplayViewManager.getReportsView().drawView()

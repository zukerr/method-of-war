from method_of_war.ui.gameplay_ui.settlement_view import *
from method_of_war.ui.gameplay_ui.map.map_view import *
from method_of_war.ui.gameplay_ui.reports.reports_list_view import *
from method_of_war.enums.gameplay_view_type import *
from method_of_war.ui.gameplay_ui.map.send_troops_view import *
from method_of_war.ui.gameplay_ui.reports.report_details_view import *
from method_of_war.ui.menu_ui.defeat_view import DefeatView
from method_of_war.ui.menu_ui.victory_view import VictoryView


class GameplayViewManager:
    __mainWindow: pygame.display
    __activeView: View
    __activeViewType: GameplayViewType

    __mapView: MapView
    __reportsView: ReportsListView
    __overviewView: SettlementView
    __sendTroopsView: SendTroopsView
    __reportDetailsView: ReportDetailsView

    __victoryView: VictoryView
    __defeatView: DefeatView

    def __init__(self, window):
        self.__mainWindow = window

        # setup gameplay view ui
        self.__overviewView = SettlementView(self.__mainWindow,
                                             preClickBuildingFunction=self.preClickBuildingView,
                                             postClickBuildingFunction=self.postClickBuildingView)
        self.__mapView = MapView(self.__mainWindow)
        self.__reportsView = ReportsListView(self.__mainWindow)
        self.__sendTroopsView = SendTroopsView(self.__mainWindow)
        self.__reportDetailsView = ReportDetailsView(self.__mainWindow)
        self.__victoryView = VictoryView(self.__mainWindow)
        self.__defeatView = DefeatView(self.__mainWindow)

        # draw views
        self.__overviewView.drawView()
        self.__activeView = self.__overviewView
        self.__activeViewType = GameplayViewType.OVERVIEW

    def switchGameplayView(self, viewType: GameplayViewType):
        if self.__activeViewType == viewType:
            return
        self.__activeView.disableView()
        if viewType == GameplayViewType.MAP:
            self.__activeView = self.__mapView
            self.__activeViewType = GameplayViewType.MAP
        elif viewType == GameplayViewType.OVERVIEW:
            self.__activeView = self.__overviewView
            self.__activeViewType = GameplayViewType.OVERVIEW
        else:
            self.__activeView = self.__reportsView
            self.__activeViewType = GameplayViewType.REPORTS
        self.__activeView.drawView()

    def preClickBuildingView(self):
        self.__activeView.disableView()

    def postClickBuildingView(self, buildingView: View, gameplayViewType: GameplayViewType = GameplayViewType.BUILDING):
        self.__activeView = buildingView
        self.__activeViewType = gameplayViewType

    def getOverview(self) -> SettlementView:
        return self.__overviewView

    def isCityHallViewActive(self) -> bool:
        return self.__activeViewType == GameplayViewType.CITY_HALL

    def isBarracksViewActive(self) -> bool:
        return self.__activeViewType == GameplayViewType.BARRACKS

    def isReportsViewActive(self) -> bool:
        return self.__activeViewType == GameplayViewType.REPORTS

    def getMapView(self) -> MapView:
        return self.__mapView

    def getSendTroopsView(self) -> SendTroopsView:
        return self.__sendTroopsView

    def getReportsView(self) -> ReportsListView:
        return self.__reportsView

    def getReportDetailsView(self) -> ReportDetailsView:
        return self.__reportDetailsView

    def setVictoryScreen(self):
        self.preClickBuildingView()
        self.__victoryView.drawView()
        self.postClickBuildingView(self.__victoryView, GameplayViewType.ENDING_SCREEN)

    def setDefeatScreen(self):
        self.preClickBuildingView()
        self.__defeatView.drawView()
        self.postClickBuildingView(self.__defeatView, GameplayViewType.ENDING_SCREEN)

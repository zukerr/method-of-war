from method_of_war.ui.gameplay_ui.settlement_view import *
from method_of_war.ui.gameplay_ui.map_view import *
from method_of_war.ui.gameplay_ui.reports_view import *
from method_of_war.enums.gameplay_view_type import *
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.barracks.barracks_view import *
from method_of_war.ui.gameplay_ui.send_troops_view import *


class GameplayViewManager:
    __mainWindow: pygame.display
    __activeView: View
    __activeViewType: GameplayViewType

    __mapView: MapView
    __reportsView: ReportsView
    __overviewView: SettlementView
    __sendTroopsView: SendTroopsView

    def __init__(self, window):
        self.__mainWindow = window

        # setup gameplay view ui
        self.__overviewView = SettlementView(self.__mainWindow,
                                             preClickBuildingFunction=self.preClickBuildingView,
                                             postClickBuildingFunction=self.postClickBuildingView)
        self.__mapView = MapView(self.__mainWindow)
        self.__reportsView = ReportsView(self.__mainWindow)

        # draw views
        self.__overviewView.drawView()
        self.__activeView = self.__overviewView
        self.__activeViewType = GameplayViewType.OVERVIEW

        # mapView.setNode(1, 2, NodeType.FRIENDLY)
        # mapView.setNode(3, 1, NodeType.ENEMY)
        # self.__reportsView.addElement(ReportElement(BattleResult.POSITIVE, AttackSize.MIDSIZED,
        #                                     "Player", "Stormwind", "Orgrimmar", (1, 2), (3, 1), 412))
        # self.__reportsView.addElement(ReportElement(BattleResult.NEUTRAL, AttackSize.SMALL,
        #                                     "Player", "Stormwind", "Orgrimmar", (1, 2), (3, 1), 351))
        # self.__reportsView.addElement(ReportElement(BattleResult.NEGATIVE, AttackSize.BIG,
        #                                     "Thrall", "Orgrimmar", "Stormwind", (3, 1), (1, 2), 289))
        # self.__reportsView.addElement(ReportElement(BattleResult.NEGATIVE, AttackSize.BIG,
        #                                     "Thrall", "Orgrimmar", "Stormwind", (3, 1), (1, 2), 272))
        # TEST SECTION END
        self.__setupMapView()
        self.__setupReportsView()
        self.__setupOverviewView()

        # test send troops view
        self.__activeView.disableView()
        self.__sendTroopsView = SendTroopsView(self.__mainWindow)
        self.__sendTroopsView.drawView()
        self.__activeView = self.__sendTroopsView
        self.__activeViewType = GameplayViewType.SEND_TROOPS
        self.__sendTroopsView.updateAvailableUnits([
            SendTroopsElement(unitColorDict["Warrior"], 10, 5, lambda: None, lambda: None, lambda: None, lambda: None, lambda: None, lambda: None),
            SendTroopsElement(unitColorDict["Paladin"], 15, 3, lambda: None, lambda: None, lambda: None, lambda: None,
                              lambda: None, lambda: None)
        ])
        self.__sendTroopsView.updateOwnerName("Thrall")
        self.__sendTroopsView.updateTargetLocation("(2, 3)")
        self.__sendTroopsView.drawView()

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
        # self.__setupView()

    def __setupView(self):
        if self.__activeViewType == GameplayViewType.MAP:
            self.__setupMapView()
        elif self.__activeViewType == GameplayViewType.OVERVIEW:
            self.__setupOverviewView()
        else:
            self.__setupReportsView()

    def __setupMapView(self):
        self.__mapView.setNode(1, 2, NodeType.FRIENDLY, False)
        self.__mapView.setNode(3, 1, NodeType.ENEMY, False)

    def __setupReportsView(self):
        # test values
        self.__reportsView.addElement(ReportElement(BattleResult.POSITIVE, AttackSize.MIDSIZED,
                                                    "Player", "Stormwind", "Orgrimmar", (1, 2), (3, 1), 412), False)
        self.__reportsView.addElement(ReportElement(BattleResult.NEUTRAL, AttackSize.SMALL,
                                                    "Player", "Stormwind", "Orgrimmar", (1, 2), (3, 1), 351), False)
        self.__reportsView.addElement(ReportElement(BattleResult.NEGATIVE, AttackSize.BIG,
                                                    "Thrall", "Orgrimmar", "Stormwind", (3, 1), (1, 2), 289), False)
        self.__reportsView.addElement(ReportElement(BattleResult.NEGATIVE, AttackSize.BIG,
                                                    "Thrall", "Orgrimmar", "Stormwind", (3, 1), (1, 2), 272), False)

    def __setupOverviewView(self):
        pass

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

# TO-DO
from mini_engine.ui.a_view import View
from method_of_war.ui.gameplay_ui.reports.report_details_bg_list_view import *
from method_of_war.ui.gameplay_ui.reports.reports_list_view import ReportElement
from mini_engine.ui import border_rect


class ReportDetailsView(View):
    __bgListView: ReportDetailsBgListView

    __rootReportElement: ReportElement

    def drawView(self):
        # draw table fundamentals
        self.__bgListView = ReportDetailsBgListView(self._window)

        self.__bgListView.addElement(ReportDetailsBgElement(grey44, "Topic"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey44, "Time"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey44, "Result"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey44, "Aggressor"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey44, "From"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey23, "Units"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey23, "Quantity"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey23, "Losses"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey44, "Defender"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey44, "Target"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey23, "Units"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey23, "Quantity"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey23, "Losses"), False)
        self.__bgListView.addElement(ReportDetailsBgElement(grey44, "Loot"), False)

        self.__bgListView.drawView()

        # draw table data
        # topic
        border_rect.draw(self._window, battleResultColorDict[self.__rootReportElement.battleResult], (166, 62, 35, 35))
        textSurface = getBigFont().render(self.__rootReportElement.topicToDisplay, True, (255, 255, 255))
        self._window.blit(textSurface, (208, 62))
        # time
        textSurface = getBigFont().render(self.__rootReportElement.timestampStr, True, (255, 255, 255))
        self._window.blit(textSurface, (166, 109))
        # result
        textSurface = getBigFont().render(self.__rootReportElement.resultString, True, (255, 255, 255))
        self._window.blit(textSurface, (166, 154))
        # aggressor
        textSurface = getBigFont().render(self.__rootReportElement.attackingPlayerName, True, (255, 255, 255))
        self._window.blit(textSurface, (166, 199))
        # from
        textSurface = getBigFont().render(self.__rootReportElement.attackingSettlementLocationStr, True,
                                          (255, 255, 255))
        self._window.blit(textSurface, (166, 244))
        # units
        self.__drawUnitSegment(287,
                               self.__rootReportElement.initialAttackingArmyDict,
                               self.__rootReportElement.attackingArmyLossesDict)
        # defender
        textSurface = getBigFont().render(self.__rootReportElement.defendingPlayerName, True,
                                          (255, 255, 255))
        self._window.blit(textSurface, (166, 424))
        # target
        textSurface = getBigFont().render(self.__rootReportElement.defendingSettlementLocationStr, True,
                                          (255, 255, 255))
        self._window.blit(textSurface, (166, 469))
        # units
        self.__drawUnitSegment(512,
                               self.__rootReportElement.initialDefendingArmyDict,
                               self.__rootReportElement.defendingArmyLossesDict)
        # loot
        self.__drawLootSegment(161, "Wood", self.__rootReportElement.lootedWood)
        self.__drawLootSegment(291, "Granite", self.__rootReportElement.lootedGranite)
        self.__drawLootSegment(421, "Iron", self.__rootReportElement.lootedIron)
        # loot summary
        lootSummaryString = str(self.__rootReportElement.lootSummary) + "/" + str(self.__rootReportElement.lootingCapacity)
        textSurface = getBigFont().render(lootSummaryString, True, (255, 255, 255))
        self._window.blit(textSurface, (813, 648))

        # no info about defender case
        if self.__rootReportElement.isFailedAttack:
            border_rect.draw(self._window, grey44, (161, 507, 836, 135))
            textSurface = getBigFont().render("All your units died in battle - no information about defender", True,
                                              (255, 255, 255))
            self._window.blit(textSurface, (169, 507))

        # draw damage done
        border_rect.draw(self._window, grey44, (450, 147, 546, 45))
        border_rect.draw(self._window, grey44, (663, 147, 333, 45))
        textSurface = getBigFont().render("Damage Done", True, (255, 255, 255))
        self._window.blit(textSurface, (455, 152))
        textSurface = getBigFont().render(str(self.__rootReportElement.damageDealt), True, (255, 255, 255))
        self._window.blit(textSurface, (670, 154))

    def __drawUnitSegment(self, y: int, initialArmy: dict, armyLosses: dict):
        keyList = list(unitColorDict.keys())
        x = 172
        width = 35
        height = 35
        for key in keyList:
            border_rect.draw(self._window, unitColorDict[key], (x, y, width, height))
            textSurface = getDefaultFont().render(str(initialArmy[key]), True,
                                                  (255, 255, 255))
            self._window.blit(textSurface, (x, y + 45))
            textSurface = getDefaultFont().render(str(armyLosses[key]), True,
                                                  (255, 255, 255))
            self._window.blit(textSurface, (x, y + 90))
            x += 45

    def __drawLootSegment(self, x: int, resourceName: str, lootedValue: int):
        y = 641
        border_rect.draw(self._window, grey44, (x, y, 130, 45))
        border_rect.draw(self._window, resourceColorDict[resourceName], (x + 5, y + 5, 35, 35))
        textSurface = getDefaultFont().render(str(lootedValue), True,
                                              (255, 255, 255))
        self._window.blit(textSurface, (x + 45, y + 5))

    def updateData(self, reportElement: ReportElement):
        self.__rootReportElement = reportElement

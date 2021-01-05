from method_of_war.ui.gameplay_ui.reports.reports_list_view import ReportElement
from typing import List


class Reports:
    _elementList: List[ReportElement]
    __maxListLength: int

    def __init__(self):
        super().__init__()
        self._elementList = []
        self.__maxListLength = 13

    def addReport(self, reportElement: ReportElement):
        if len(self._elementList) >= self.__maxListLength:
            self._elementList.pop(0)
        self._elementList.append(reportElement)

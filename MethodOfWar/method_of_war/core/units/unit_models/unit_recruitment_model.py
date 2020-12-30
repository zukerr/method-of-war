from method_of_war.core.units.unit_models.a_unit import Unit
from method_of_war.ui.gameplay_ui.building_views.barracks.recruitment_queue_list_view import RecruitmentQueueElement
from method_of_war.ui.ui_global import *


class UnitRecruitmentModel:
    __unit: Unit
    __recruitmentQueueElement: RecruitmentQueueElement

    def __init__(self, unit: Unit):
        self.__unit = unit
        makeTextDark = False
        if self.__unit.getName() == "Rogue":
            makeTextDark = True
        self.__recruitmentQueueElement = \
            RecruitmentQueueElement(int(self.__unit.getResourceRequirement().timeInSeconds),
                                    unitColorDict[self.__unit.getName()],
                                    0, makeTextDark=makeTextDark,
                                    realTimeToFinish=self.__unit.getResourceRequirement().timeInSeconds)

    def getRecruitmentQueueElement(self) -> RecruitmentQueueElement:
        return self.__recruitmentQueueElement

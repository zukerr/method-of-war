from mini_engine.ui.a_view import *
from method_of_war.ui.gameplay_ui.building_views import building_header_view
from method_of_war.ui.gameplay_ui.building_views.barracks.recruitment_queue_bg_list_view import *
from method_of_war.ui.gameplay_ui.building_views.barracks.recruitment_queue_list_view import *
from method_of_war.ui.gameplay_ui.building_views.city_hall.city_hall_available_buildings_list_view import *


class BarracksView(View):
    __buildingLevel: int
    __availableRecruitsView: CityHallAvailableBuildingsListView

    def __init__(self, window, buildingLevel: int):
        super().__init__(window)
        self.__buildingLevel = buildingLevel

    def drawView(self):
        # draw bg
        border_rect.draw(self._window, grey44, (0, 57, 997, 663))
        # draw building header view
        headerView = building_header_view.BuildingHeaderView(self._window, buildingColorDict["Barracks"],
                                                             "Barracks (Level " + str(self.__buildingLevel) + ")",
                                                             "In Barracks you can recruit units."
                                                             " The higher level Barracks have,"
                                                             " the shorter are unit recruit times.")
        headerView.drawView()
        # draw recruitment queue bg list view
        recruitmentQueueBgView = RecruitmentQueueBgListView(self._window)
        for i in range(8):
            recruitmentQueueBgView.addElement(RecruitmentQueueBgElement(i + 1), drawImmediately=False)
        recruitmentQueueBgView.drawView()
        # draw recruitment queue
        recruitmentQueueView = RecruitmentQueueListView(self._window)
        recruitmentQueueView.addElement(RecruitmentQueueElement(timeToFinishInSeconds=5,
                                                                bgColor=unitColorDict["Warlock"],
                                                                progressBarProgress=0.75))
        recruitmentQueueView.addElement(RecruitmentQueueElement(timeToFinishInSeconds=21,
                                                                bgColor=unitColorDict["Rogue"],
                                                                progressBarProgress=0.0, makeTextDark=True))
        recruitmentQueueView.drawView()
        # availible recruits view
        self.__availableRecruitsView = CityHallAvailableBuildingsListView(window=self._window,
                                                                   columnNameList=["Unit", "Requirements", "Recruit"],
                                                                   defaultY=378)
        self.__availableRecruitsView.addElement(AvailableBuildingElement("Warlock", "Warlock", 92, 502, 1272, 201,
                                                                  "--> Recruit", isUnit=True))
        self.__availableRecruitsView.addElement(AvailableBuildingElement("Rogue", "Rogue", 92, 502, 1272, 201,
                                                                  "--> Recruit", isUnit=True))
        self.__availableRecruitsView.drawView()

    def disableView(self):
        self.__availableRecruitsView.disableView()

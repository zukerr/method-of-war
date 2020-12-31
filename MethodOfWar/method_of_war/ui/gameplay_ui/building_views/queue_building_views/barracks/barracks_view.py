from method_of_war.ui.gameplay_ui.building_views import building_header_view
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.barracks.recruitment_queue_bg_list_view import *
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.barracks.recruitment_queue_list_view import *
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.city_hall.city_hall_available_buildings_list_view import *
from method_of_war.ui.gameplay_ui.building_views.queue_building_views.queue_building_view import *


class BarracksView(QueueBuildingView):

    def __init__(self, window, buildingLevel: int):
        super().__init__(window)
        self._level = buildingLevel

    def drawView(self):
        # draw bg
        border_rect.draw(self._window, grey44, (0, 57, 997, 663))

        # draw building header view
        headerView = building_header_view.BuildingHeaderView(self._window, buildingColorDict["Barracks"],
                                                             "Barracks (Level " + str(self._level) + ")",
                                                             "In Barracks you can recruit units."
                                                             " The higher level Barracks have,"
                                                             " the shorter are unit recruit times.")
        headerView.drawView()

        # draw recruitment queue
        self.drawQueue()

        # available recruits view
        self.drawAvailable()

    def _drawQueueSetup(self):
        # draw recruitment queue bg list view
        border_rect.draw(self._window, grey44, (0, 207, 997, 126))
        recruitmentQueueBgView = RecruitmentQueueBgListView(self._window)
        for i in range(8):
            recruitmentQueueBgView.addElement(RecruitmentQueueBgElement(i + 1), drawImmediately=False)
        recruitmentQueueBgView.drawView()
        self._queueListView = RecruitmentQueueListView(self._window)

    def _drawAvailableSetup(self):
        self._availableListView = CityHallAvailableBuildingsListView(window=self._window,
                                                                     columnNameList=["Unit", "Requirements",
                                                                                     "Recruit"],
                                                                     defaultY=378)

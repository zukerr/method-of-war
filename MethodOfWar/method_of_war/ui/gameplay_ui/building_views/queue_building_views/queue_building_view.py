from method_of_war.ui.gameplay_ui.building_views.queue_building_views.city_hall.city_hall_available_buildings_list_view import *
from mini_engine.ui.a_list_view_standard import ListViewStandard


class QueueBuildingView(View, ABC):
    _level: int
    __queue = []
    _availableList: List[AvailableBuildingElement] = []

    _queueListView: ListViewStandard = None
    _availableListView: CityHallAvailableBuildingsListView = None

    @abstractmethod
    def _drawQueueSetup(self):
        pass

    def drawQueue(self):
        # draw queue bg
        self._drawQueueSetup()
        self._queueListView.clearElements()
        for elem in self.__queue:
            self._queueListView.addElement(elem, False)
        self._queueListView.drawView()

    @abstractmethod
    def _drawAvailableSetup(self):
        pass

    def drawAvailable(self):
        self._drawAvailableSetup()
        self._availableListView.clearElements()
        for elem in self._availableList:
            self._availableListView.addElement(elem, False)
        self._availableListView.drawView()

    def disableView(self):
        if self._queueListView is not None:
            self._queueListView.disableView()
        if self._availableListView is not None:
            self._availableListView.disableView()

    def updateLevel(self, level: int):
        self._level = level

    def updateQueue(self, queue):
        self.__queue = queue

    def updateAvailableList(self, availableList: List[AvailableBuildingElement]):
        self._availableList = availableList

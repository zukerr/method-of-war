from method_of_war.core.buildings.barracks import *


class PlayerBarracks(Barracks):

    def levelUp(self):
        super().levelUp()
        # global_gameplay_view_manager.globalGameplayViewManager.getOverview().getBarracks().updateLevel(self._level)
        self.__syncView()

    # queue
    def addUnitToQueue(self, unit: Unit):
        super().addUnitToQueue(unit)
        global_gameplay_view_manager.globalGameplayViewManager.getOverview().getBarracks().updateQueue(self._getUiReadableQueue())

    def _updateQueueContent(self, timePassed: float):
        super()._updateQueueContent(timePassed)
        global_gameplay_view_manager.globalGameplayViewManager.getOverview().getBarracks().updateQueue(
            self._getUiReadableQueue())
        if global_gameplay_view_manager.globalGameplayViewManager.isBarracksViewActive():
            global_gameplay_view_manager.globalGameplayViewManager.getOverview().getBarracks().drawQueue()

    # available units
    def setupAvailableUnits(self):
        super().setupAvailableUnits()
        self.__syncView()

    def __redrawBarracksView(self):
        if global_gameplay_view_manager.globalGameplayViewManager.isBarracksViewActive():
            global_gameplay_view_manager.globalGameplayViewManager.getOverview().getBarracks().disableView()
            global_gameplay_view_manager.globalGameplayViewManager.getOverview().getBarracks().drawView()

    def __syncView(self):
        global_gameplay_view_manager.globalGameplayViewManager.getOverview().getBarracks().updateLevel(self._level)
        global_gameplay_view_manager.globalGameplayViewManager.getOverview().getBarracks().updateAvailableList(self._availableRecruitsList)

from mini_engine.ui.a_view import *
from mini_engine.ui.a_list_view import *
from method_of_war.ui.ui_global import *
from mini_engine.ui import button
from mini_engine.util.extensions import *
from typing import List
from method_of_war.ui.gameplay_ui.building_views.city_hall.a_building_list_view import *


class NotAvailableBuildingElement:
    __maxBuildingReq: int = 4
    buildingName: str
    buildingColor: (int, int, int)
    buildingReqNameList: List[str]
    buildingReqLevelList: List[int]
    buildingReqColorList = []

    def __init__(self, buildingName: str, buildingReqNameList: List[str], buildingReqLevelList: List[int]):
        if len(buildingReqNameList) > self.__maxBuildingReq:
            print("ERROR: Tried to create not available building list element in city hall with wrong args!")
            self.buildingReqNameList = []
            self.buildingReqColorList = []
        else:
            self.buildingName = buildingName
            self.buildingColor = buildingColorDict[self.buildingName]
            self.buildingReqNameList = buildingReqNameList
            self.buildingReqLevelList = buildingReqLevelList
            self.buildingReqColorList = []
            for i in range(len(buildingReqNameList)):
                self.buildingReqColorList.append(buildingColorDict[self.buildingReqNameList[i]])


class CityHallNotAvailableBuildingsListView(BuildingListView):

    def __init__(self, window, defaultY: int = 630):
        super().__init__(window, maxElements=2, defaultX=0, defaultY=defaultY, elementWidth=997, elementHeight=45)

    def _drawElementDetails(self, element: NotAvailableBuildingElement, transform: (int, int, int, int)):
        # building info
        self._drawBuildingInfo(transform, element.buildingName, element.buildingColor)
        # requirements bg
        border_rect.draw(self._window, grey44, (transform[0] + 248, transform[1], 749, transform[3]))
        reqTransform: (int, int, int, int) = (transform[0] + 248, transform[1], 187, transform[3])
        # building requirements
        for i in range(len(element.buildingReqNameList)):
            self._drawRequirementSegment(reqTransform,
                                         element.buildingReqColorList[i],
                                         str(element.buildingReqNameList[i])
                                         + "(" + str(element.buildingReqLevelList[i]) + ")")
            reqTransform: (int, int, int, int) = (reqTransform[0] + reqTransform[2],
                                                  reqTransform[1], reqTransform[2], reqTransform[3])

    def _drawViewSetup(self):
        # draw title row bg
        startingY = self._defaultY - self._elementHeight
        border_rect.draw(self._window, grey44, (0, startingY, 997, self._elementHeight))
        # draw not available subtitle bg
        border_rect.draw(self._window, grey23, (0, startingY, 248, self._elementHeight))
        # draw not available subtitle
        textSurface = getDefaultFont().render("Not Available", True, (255, 255, 255))
        self._window.blit(textSurface, (5, startingY))
        # draw requirements subtitle bg
        border_rect.draw(self._window, grey23, (248, startingY, 749, self._elementHeight))
        # draw requirements subtitle
        textSurface = getDefaultFont().render("Requirements", True, (255, 255, 255))
        self._window.blit(textSurface, (253, startingY))

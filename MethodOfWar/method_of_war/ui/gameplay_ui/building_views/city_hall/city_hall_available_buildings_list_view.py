from mini_engine.ui.a_view import *
from mini_engine.ui.a_list_view import *
from method_of_war.ui.ui_global import *
from mini_engine.ui import button
from mini_engine.util.extensions import *
from typing import List
from method_of_war.ui.gameplay_ui.building_views.city_hall.a_building_list_view import *


class AvailableBuildingElement:
    buildingName: str
    buildingIconColor: (int, int, int)
    buildingTitle: str
    buildingWoodReq: int
    buildingGraniteReq: int
    buildingIronReq: int
    buildingTime: str
    buttonText: str
    buttonFunction = lambda: None

    def __init__(self, buildingName: str, buildingTitle: str, buildingWoodReq: int, buildingGraniteReq: int,
                 buildingIronReq: int, buildingTime: int, buttonText: str, isUnit: bool = False, buttonFunction=lambda: None):
        self.buildingName = buildingName
        if not isUnit:
            self.buildingIconColor = buildingColorDict[buildingName]
        else:
            self.buildingIconColor = unitColorDict[buildingName]
        self.buildingTitle = buildingTitle
        self.buildingWoodReq = buildingWoodReq
        self.buildingGraniteReq = buildingGraniteReq
        self.buildingIronReq = buildingIronReq
        self.buildingTime = getMinutesSecondsFromSeconds(buildingTime)
        self.buttonText = buttonText
        self.buttonFunction = buttonFunction


class CityHallAvailableBuildingsListView(BuildingListView):
    __buttonsList: List[button.Button] = []
    __columnNameList: List[str]

    def __init__(self, window, columnNameList=None, defaultY=360):
        super().__init__(window, maxElements=10, defaultX=0, defaultY=defaultY, elementWidth=997, elementHeight=45)
        if columnNameList is None:
            columnNameList = ["Buildings", "Requirements", "Build"]
        self.__columnNameList = columnNameList

    def _drawElementDetails(self, element: AvailableBuildingElement, transform: (int, int, int, int)):
        # building info
        self._drawBuildingInfo(transform, element.buildingTitle, element.buildingIconColor)
        # requirements bg
        border_rect.draw(self._window, grey44, (transform[0] + 248, transform[1], 492, transform[3]))
        reqTransform = (transform[0] + 248, transform[1], 130, transform[3])
        # requirement wood
        self._drawRequirementSegment(reqTransform, resourceColorDict["Wood"], str(element.buildingWoodReq))
        reqTransform = (reqTransform[0] + reqTransform[2], reqTransform[1], reqTransform[2], reqTransform[3])
        # requirement granite
        self._drawRequirementSegment(reqTransform, resourceColorDict["Granite"], str(element.buildingGraniteReq))
        reqTransform = (reqTransform[0] + reqTransform[2], reqTransform[1], reqTransform[2], reqTransform[3])
        # requirement iron
        self._drawRequirementSegment(reqTransform, resourceColorDict["Iron"], str(element.buildingIronReq))
        reqTransform = (reqTransform[0] + reqTransform[2], reqTransform[1], 102, reqTransform[3])
        # required time bg
        border_rect.draw(self._window, grey44, reqTransform)
        # required time text
        textSurface = getDefaultFont().render(element.buildingTime, True, (255, 255, 255))
        self._window.blit(textSurface, (transform[0] + 683, transform[1] + 5))
        # build button bg
        border_rect.draw(self._window, grey44, (transform[0] + 740, transform[1], 257, transform[3]))

        # build button
        def addedDraw():
            # build button text
            textSurface = getDefaultFont().render(element.buttonText, True, (255, 255, 255))
            self._window.blit(textSurface, (transform[0] + 750, transform[1] + 5))

        buildButton = button.Button(self._window, darkGreen,
                                    (transform[0] + 745, transform[1] + 5, 247, transform[3] - 10),
                                    1, borderDefaultColor, addedDraw=addedDraw)

        def onClick():
            print("clicked build button!")
            element.buttonFunction()
            # update button text
            # btnWordList = element.buttonText.split()
            # btnUpgradeLevel = int(btnWordList[len(btnWordList) - 1])
            # element.buttonText = "--> Level " + str(btnUpgradeLevel + 1)

        buildButton.addListener(onClick)
        buildButton.draw()
        self.__buttonsList.append(buildButton)

    def _drawViewSetup(self):
        self.disableView()
        startingY = self._defaultY - self._elementHeight
        # draw title row bg
        border_rect.draw(self._window, grey44, (0, startingY, 997, self._elementHeight))
        # draw buildings subtitle bg
        border_rect.draw(self._window, grey23, (0, startingY, 248, self._elementHeight))
        # draw buildings subtitle
        textSurface = getDefaultFont().render(self.__columnNameList[0], True, (255, 255, 255))
        self._window.blit(textSurface, (5, startingY))
        # draw requirements subtitle bg
        border_rect.draw(self._window, grey23, (248, startingY, 492, self._elementHeight))
        # draw requirements subtitle
        textSurface = getDefaultFont().render(self.__columnNameList[1], True, (255, 255, 255))
        self._window.blit(textSurface, (253, startingY))
        # draw build subtitle bg
        border_rect.draw(self._window, grey23, (740, startingY, 257, self._elementHeight))
        # draw build subtitle
        textSurface = getDefaultFont().render(self.__columnNameList[2], True, (255, 255, 255))
        self._window.blit(textSurface, (745, startingY))

    def disableView(self):
        for btn in self.__buttonsList:
            btn.setActive(False)
            btn.setReadyForDelete()

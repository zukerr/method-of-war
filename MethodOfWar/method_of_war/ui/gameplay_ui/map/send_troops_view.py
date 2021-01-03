from method_of_war.ui.gameplay_ui.map.send_troops_table_list_view import *


class SendTroopsView(View):
    __targetLocation: str = ""
    __ownerName: str = ""
    __elementList: List[SendTroopsElement] = []
    __resetAllListener = lambda: None
    __sendAttackListener = lambda: None

    __buttonList: List[button.Button] = []

    __sendTroopsListView: SendTroopsTableListView = None

    def drawView(self):
        # draw bg
        border_rect.draw(self._window, grey44, (0, 57, 997, 663))
        # draw title bg
        border_rect.draw(self._window, grey44, (0, 57, 997, 68))
        # draw title text
        textSurface = getVeryBigFont().render('Send Troops', True, (255, 255, 255))
        self._window.blit(textSurface, (10, 69))
        # draw inner bg
        border_rect.draw(self._window, grey44, (0, 125, 997, 595))
        # draw inner dark bg
        border_rect.draw(self._window, grey23, (32, 182, 934, 481))
        # draw target section bg
        border_rect.draw(self._window, grey44, (741, 196, 211, 142))
        # draw target section text
        textValue: str = "Target: " + self.__targetLocation + " Owner: " + self.__ownerName
        blit_text(self._window, (950, 142), textValue, (750, 196), getVeryBigFont(), (255, 255, 255))

        # draw main action buttons
        # reset all button
        resetAllButton = GreenButton(self._window, (741, 526, 211, 46), "Reset All", getBigFont())

        def resetOnClick():
            self.__resetAllListener()

        resetAllButton.addListener(resetOnClick)
        resetAllButton.draw()
        self.__buttonList.append(resetAllButton)

        # send attack button
        sendAttackButton = GreenButton(self._window, (741, 602, 211, 46), "Send Attack", getBigFont())

        def sendAttackOnClick():
            self.__sendAttackListener()

        sendAttackButton.addListener(sendAttackOnClick)
        sendAttackButton.draw()
        self.__buttonList.append(sendAttackButton)

        # draw table
        self.__sendTroopsListView = SendTroopsTableListView(self._window)
        for elem in self.__elementList:
            self.__sendTroopsListView.addElement(elem, False)
        self.__sendTroopsListView.drawView()

    def updateAvailableUnits(self, elementList: List[SendTroopsElement]):
        self.__elementList = elementList

    def updateTargetLocation(self, targetLocation: str):
        self.__targetLocation = targetLocation

    def updateOwnerName(self, ownerName: str):
        self.__ownerName = ownerName

    def updateResetAllListener(self, newListener):
        self.__resetAllListener = newListener

    def updateSendAttackListener(self, newListener):
        self.__sendAttackListener = newListener

    def disableView(self):
        for btn in self.__buttonList:
            btn.setActive(False)
            btn.setReadyForDelete()
        # disable list view
        if self.__sendTroopsListView is not None:
            self.__sendTroopsListView.disableView()

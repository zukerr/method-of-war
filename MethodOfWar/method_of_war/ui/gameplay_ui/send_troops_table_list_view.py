from mini_engine.ui import button
from mini_engine.util.extensions import *
from mini_engine.ui.a_list_view import *
from method_of_war.ui.green_button import GreenButton


class SendTroopsElement:
    iconColor: (int, int, int)
    availableUnits: int
    currentUnits: int
    # on click functions
    add1 = lambda: None
    add5 = lambda: None
    remove1 = lambda: None
    remove5 = lambda: None
    addAll = lambda: None
    reset = lambda: None

    def __init__(self, iconColor: (int, int, int), availableUnits: int, currentUnits: int, add1, add5, remove1, remove5, addAll, reset):
        self.iconColor = iconColor
        self.availableUnits = availableUnits
        self.currentUnits = currentUnits
        self.add1 = add1
        self.add5 = add5
        self.remove1 = remove1
        self.remove5 = remove5
        self.addAll = addAll
        self.reset = reset


class SendTroopsTableListView(ListView):
    __buttonList: List[button.Button] = []

    def __init__(self, window):
        super().__init__(window, maxElements=11, defaultX=46, defaultY=196, elementWidth=628, elementHeight=32)

    def __drawElementGreenButton(self, x: int, y: int, width: int, text: str, onClick):
        tempButton = GreenButton(self._window, (x, y, width, 32), text, getDefaultFont())
        tempButton.addListener(onClick)
        tempButton.draw()
        self.__buttonList.append(tempButton)

    def _drawElementDetails(self, element: SendTroopsElement, transform: (int, int, int, int)):
        # draw element bg
        border_rect.draw(self._window, grey23, transform)
        # draw icon
        border_rect.draw(self._window, element.iconColor, (transform[0], transform[1], 32, transform[3]))
        # draw current units text
        textSurface = getDefaultFont().render(str(element.currentUnits), True, (255, 255, 255))
        self._window.blit(textSurface, (88, transform[1]))
        # draw available units text
        textSurface = getDefaultFont().render("(" + str(element.availableUnits) + ")", True, (255, 255, 255))
        self._window.blit(textSurface, (126, transform[1]))

        # draw add 1 button
        def onClickAdd1():
            print("Clicked add 1!")
            element.add1()
        self.__drawElementGreenButton(x=174, y=transform[1], width=64, text="add 1", onClick=onClickAdd1)

        # draw add 5 button
        def onClickAdd5():
            print("Clicked add 5!")
            element.add5()
        self.__drawElementGreenButton(x=248, y=transform[1], width=64, text="add 5", onClick=onClickAdd5)

        # draw remove 1 button
        def onClickRemove1():
            print("Clicked remove 1!")
            element.remove1()
        self.__drawElementGreenButton(x=322, y=transform[1], width=96, text="remove 1", onClick=onClickRemove1)

        # draw remove 5 button
        def onClickRemove5():
            print("Clicked remove 5!")
            element.remove5()
        self.__drawElementGreenButton(x=428, y=transform[1], width=96, text="remove 5", onClick=onClickRemove5)

        # draw add all button
        def onClickAddAll():
            print("Clicked add all!")
            element.addAll()
        self.__drawElementGreenButton(x=534, y=transform[1], width=73, text="add all", onClick=onClickAddAll)

        # draw reset button
        def onClickReset():
            print("Clicked reset!")
            element.reset()
        self.__drawElementGreenButton(x=617, y=transform[1], width=57, text="reset", onClick=onClickReset)

    def _drawViewSetup(self):
        # safety call, irrelevant in most cases
        self.disableView()

    def disableView(self):
        for btn in self.__buttonList:
            btn.setActive(False)
            btn.setReadyForDelete()

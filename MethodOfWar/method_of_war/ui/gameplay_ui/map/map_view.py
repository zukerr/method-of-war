import pygame
from mini_engine.ui import border_rect
from mini_engine.ui.a_view import *
from method_of_war.ui.ui_global import *
from mini_engine.ui import button
from typing import List
from method_of_war.enums.map_node_type import *
from mini_engine.ui import border_progress_bar


class MapNode:
    __x: int
    __y: int
    __color: (int, int, int)
    __highlightColor: (int, int, int)
    __nodeType: NodeType
    __colorsDict = {
        NodeType.FRIENDLY: (10, 43, 0),
        NodeType.EMPTY: (44, 44, 44),
        NodeType.ENEMY: (48, 10, 0)
    }
    __highlightColorsDict = {
        NodeType.FRIENDLY: (17, 71, 0),
        NodeType.EMPTY: (80, 80, 80),
        NodeType.ENEMY: (81, 17, 0)
    }
    __button: button.Button = None
    buttonListener = lambda: None

    usesProgressBar: bool = False
    progressBarFillAmount: float = 1
    progressBarText: str = ""

    def __init__(self, x: int, y: int, nodeType: NodeType, buttonListener=lambda: None):
        self.__x = x
        self.__y = y
        self.__nodeType = nodeType
        self.__color = self.__colorsDict[self.__nodeType]
        self.__highlightColor = self.__highlightColorsDict[self.__nodeType]
        self.buttonListener = buttonListener
        if (self.__nodeType == NodeType.ENEMY) or (self.__nodeType == NodeType.FRIENDLY):
            self.usesProgressBar = True
            self.progressBarFillAmount = 1
            self.progressBarText = ""

    def getColor(self) -> (int, int, int):
        return self.__color

    def getHighlightColor(self) -> (int, int, int):
        return self.__highlightColor

    def getX(self) -> int:
        return self.__x

    def getY(self) -> int:
        return self.__y

    def getNodeType(self) -> NodeType:
        return self.__nodeType

    def setButton(self, bindButton: button.Button):
        self.__button = bindButton

    def getButton(self) -> button.Button:
        return self.__button


class MapView(View):
    __topLeftGridCorner: (int, int) = (124, 89)
    __nodeSize: (int, int) = (150, 150)
    __grid: List[List[MapNode]]

    def __init__(self, window):
        super().__init__(window)
        self.__setupGrid()

    def __setupGrid(self):
        self.__grid = []
        for i in range(5):
            self.__grid.append([])
            for j in range(4):
                self.__grid[i].append(MapNode(i, j, NodeType.EMPTY))

    def __drawNode(self, mapNode: MapNode):
        previousNode = self.__grid[mapNode.getX()][mapNode.getY()]
        if previousNode is not None:
            if previousNode.getButton() is not None:
                previousNode.getButton().setInteractive(False)
                previousNode.getButton().setReadyForDelete()

        nodeTransform = (self.__topLeftGridCorner[0] + (mapNode.getX() * self.__nodeSize[0]),
                         self.__topLeftGridCorner[1] + (mapNode.getY() * self.__nodeSize[1]),
                         self.__nodeSize[0],
                         self.__nodeSize[1])

        def addedDraw():
            if mapNode.getNodeType() != NodeType.EMPTY:
                # draw banner
                self._window.blit(mapNodeBannersDict[mapNode.getNodeType()], (nodeTransform[0], nodeTransform[1]))
                # draw settlement hp bar
                border_progress_bar.draw(self._window,
                                         (nodeTransform[0], nodeTransform[1] + 130, nodeTransform[2], 20),
                                         mapNode.progressBarFillAmount,
                                         mapNode.progressBarText,
                                         getSmallFont())

        nodeButton = button.Button(self._window, mapNode.getColor(), nodeTransform, 1, borderDefaultColor,
                                   highlightColor=mapNode.getHighlightColor(), addedDraw=addedDraw)
        # nodeButton.addListener(lambda: print("just clicked (" + str(mapNode.getX()) + ", " + str(mapNode.getY()) + ")"))
        nodeButton.addListener(mapNode.buttonListener)
        nodeButton.draw()
        mapNode.setButton(nodeButton)

    def __drawAllNodes(self):
        for i in range(5):
            for j in range(4):
                self.__drawNode(self.__grid[i][j])

    def setNode(self, x: int, y: int, nodeType: NodeType,
                drawImmediately: bool = True, nodeButtonListener=lambda: None):
        previousNode = self.__grid[x][y]
        if previousNode is not None:
            if previousNode.getButton() is not None:
                previousNode.getButton().setInteractive(False)
                previousNode.getButton().setReadyForDelete()
        self.__grid[x][y] = MapNode(x, y, nodeType, nodeButtonListener)
        if drawImmediately:
            self.drawView()

    def updateNodeProgressBar(self, x: int, y: int, newFillAmount: float, newText: str):
        if self.__grid[x][y] is not None:
            if self.__grid[x][y].usesProgressBar:
                self.__grid[x][y].progressBarFillAmount = newFillAmount
                self.__grid[x][y].progressBarText = newText
                print("progressBarText after update = " + self.__grid[x][y].progressBarText)
            else:
                print("Tried to update node that does not use progress bar.")
        else:
            print("Tried to update non existing map node.")

    def drawView(self):
        print("drawing map view")
        # bg
        border_rect.draw(self._window, (23, 23, 23), (0, 57, 997, 663), 1, borderDefaultColor)
        # grid bg
        border_rect.draw(self._window, (23, 23, 23),
                         (self.__topLeftGridCorner[0], self.__topLeftGridCorner[1], 750, 600), 1, borderDefaultColor)
        # all nodes in grid
        self.__drawAllNodes()

    def disableView(self):
        print("disabling map view")
        # border_rect.draw(self._window, (23, 23, 23), (0, 57, 997, 663), 1, borderDefaultColor)
        for i in range(5):
            for j in range(4):
                buttonToDelete = self.__grid[i][j].getButton()
                buttonToDelete.setInteractive(False)
                buttonToDelete.setReadyForDelete()
                del buttonToDelete

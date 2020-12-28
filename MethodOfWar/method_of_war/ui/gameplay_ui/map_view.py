import pygame
from mini_engine.ui import border_rect
from mini_engine.ui.a_view import *
from method_of_war.ui.ui_global import *
from mini_engine.ui import button
from typing import List
from method_of_war.enums.map_node_type import *


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

    def __init__(self, x: int, y: int, nodeType: NodeType):
        self.__x = x
        self.__y = y
        self.__nodeType = nodeType
        self.__color = self.__colorsDict[self.__nodeType]
        self.__highlightColor = self.__highlightColorsDict[self.__nodeType]

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

        nodeButton = button.Button(self._window, mapNode.getColor(), nodeTransform, 1, borderDefaultColor,
                                   highlightColor=mapNode.getHighlightColor())
        nodeButton.addListener(lambda: print("just clicked (" + str(mapNode.getX()) + ", " + str(mapNode.getY()) + ")"))
        nodeButton.draw()
        mapNode.setButton(nodeButton)

    def __drawAllNodes(self):
        for i in range(5):
            for j in range(4):
                self.__drawNode(self.__grid[i][j])

    def setNode(self, x: int, y: int, nodeType: NodeType, drawImmediately: bool = True):
        previousNode = self.__grid[x][y]
        if previousNode is not None:
            if previousNode.getButton() is not None:
                previousNode.getButton().setInteractive(False)
                previousNode.getButton().setReadyForDelete()
        self.__grid[x][y] = MapNode(x, y, nodeType)
        if drawImmediately:
            self.drawView()

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

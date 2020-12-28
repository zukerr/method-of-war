import pygame
from method_of_war.enums.attack_size import *
from method_of_war.enums.battle_result import *


# default elements
borderDefaultColor = (112, 112, 112)
iconTempColor = (0, 80, 80)
defaultRed = (255, 0, 0)
defaultGreen = (0, 255, 85)
defaultYellow = (255, 238, 0)
grey44 = (44, 44, 44)
grey23 = (23, 23, 23)
darkGreen = (1, 43, 0)

# default attack size colors
attackSizeColorDict = {
    AttackSize.SMALL: (174, 236, 0),
    AttackSize.MIDSIZED: (236, 181, 0),
    AttackSize.BIG: (112, 0, 0)
}
battleResultColorDict = {
    BattleResult.NEGATIVE: defaultRed,
    BattleResult.NEUTRAL: defaultYellow,
    BattleResult.POSITIVE: defaultGreen
}
unitColorDict = {
    "Mage": (105, 204, 240),
    "Priest": (255, 255, 255),
    "Warlock": (148, 130, 201),
    "Druid": (255, 125, 10),
    "Rogue": (255, 245, 105),
    "Monk": (0, 255, 150),
    "Shaman": (0, 112, 222),
    "Hunter": (171, 212, 115),
    "Warrior": (199, 156, 110),
    "Paladin": (245, 140, 186),
    "Death Knight": (196, 31, 59)
}
resourceColorDict = {
    "Wood": (0, 194, 0),
    "Granite": (142, 142, 142),
    "Iron": (0, 128, 129),
    "All": (0, 0, 0)
}
buildingColorDict = {
    "City Hall": (163, 48, 201),
    "Lumber Mill": resourceColorDict["Wood"],
    "Quarry": resourceColorDict["Granite"],
    "Mine": resourceColorDict["Iron"],
    "Barracks": (189, 255, 0),
    "Warehouse": (255, 188, 10)
}


def getDefaultFont():
    return pygame.font.SysFont('Arial', 20)


def getSmallFont():
    return pygame.font.SysFont('Arial', 14)


def getBigFont():
    return pygame.font.SysFont('Arial', 24)


def getVeryBigFont():
    return pygame.font.SysFont('Arial', 32)

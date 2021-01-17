import pygame
from method_of_war.enums.attack_size import *
from method_of_war.enums.battle_result import *
from pathlib import *
import os
from method_of_war.enums.map_node_type import *

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


def getFontSize100():
    return pygame.font.SysFont('Arial', 100)


# setup game files
__gameFilesPath = Path(__file__).resolve().parent.parent.joinpath("game_files")


def __getGameFile(pathStr: str):
    return os.path.abspath(__gameFilesPath.joinpath(pathStr))


# game icon image
gameIcon = pygame.image.load(__getGameFile("game_icon/icon_32x32.png"))

# building view images
__buildingViewBarracks = pygame.image.load(__getGameFile("building_view_buildings/barracks_150x150.png"))
__buildingViewCityHall = pygame.image.load(__getGameFile("building_view_buildings/city_hall_150x150.png"))
__buildingViewLumberMill = pygame.image.load(__getGameFile("building_view_buildings/lumber_mill_150x150.png"))
__buildingViewMine = pygame.image.load(__getGameFile("building_view_buildings/mine_150x150.png"))
__buildingViewQuarry = pygame.image.load(__getGameFile("building_view_buildings/quarry_150x150.png"))
__buildingViewWarehouse = pygame.image.load(__getGameFile("building_view_buildings/warehouse_150x150.png"))

# overview building images
__overviewBarracks = pygame.image.load(__getGameFile("overview_buildings/barracks.png"))
__overviewCityHall = pygame.image.load(__getGameFile("overview_buildings/city_hall.png"))
__overviewLumberMill = pygame.image.load(__getGameFile("overview_buildings/lumber_mill.png"))
__overviewMine = pygame.image.load(__getGameFile("overview_buildings/mine.png"))
__overviewQuarry = pygame.image.load(__getGameFile("overview_buildings/quarry.png"))
__overviewWarehouse = pygame.image.load(__getGameFile("overview_buildings/warehouse.png"))

# building icons
__iconBarracks = pygame.image.load(__getGameFile("building_icons_35px/barracks_35x35.png"))
__iconCityHall = pygame.image.load(__getGameFile("building_icons_35px/city_hall_35x35.png"))
__iconLumberMill = pygame.image.load(__getGameFile("building_icons_35px/lumber_mill_35x35.png"))
__iconMine = pygame.image.load(__getGameFile("building_icons_35px/mine_35x35.png"))
__iconQuarry = pygame.image.load(__getGameFile("building_icons_35px/quarry_35x35.png"))
__iconWarehouse = pygame.image.load(__getGameFile("building_icons_35px/warehouse_35x35.png"))

# top action bar buttons icons
__iconOverview = pygame.image.load(__getGameFile("top_action_bar_button_icons/overview_icon.png"))
__iconMap = pygame.image.load(__getGameFile("top_action_bar_button_icons/map_icon.png"))
__iconReports = pygame.image.load(__getGameFile("top_action_bar_button_icons/reports_icon.png"))

# map node icons
__iconEnemyBanner = pygame.image.load(__getGameFile("map_node_icons/map_node_banner_enemy.png"))
__iconFriendlyBanner = pygame.image.load(__getGameFile("map_node_icons/map_node_banner_friendly.png"))

# game result screen frames
__victoryFrame = pygame.image.load(__getGameFile("game_result_frames/victory_bg.png"))
__defeatFrame = pygame.image.load(__getGameFile("game_result_frames/defeat_bg.png"))

buildingImage150pxDict = {
    "City Hall": __buildingViewCityHall,
    "Lumber Mill": __buildingViewLumberMill,
    "Quarry": __buildingViewQuarry,
    "Mine": __buildingViewMine,
    "Barracks": __buildingViewBarracks,
    "Warehouse": __buildingViewWarehouse
}

buildingImageOverviewDict = {
    "City Hall": __overviewCityHall,
    "Lumber Mill": __overviewLumberMill,
    "Quarry": __overviewQuarry,
    "Mine": __overviewMine,
    "Barracks": __overviewBarracks,
    "Warehouse": __overviewWarehouse
}

buildingIcons35pxDict = {
    "City Hall": __iconCityHall,
    "Lumber Mill": __iconLumberMill,
    "Quarry": __iconQuarry,
    "Mine": __iconMine,
    "Barracks": __iconBarracks,
    "Warehouse": __iconWarehouse
}

topActionBarIconsDict = {
    "Overview": __iconOverview,
    "Map": __iconMap,
    "Reports": __iconReports
}

mapNodeBannersDict = {
    NodeType.FRIENDLY: __iconFriendlyBanner,
    NodeType.ENEMY: __iconEnemyBanner
}

gameResultFrameDict = {
    "Victory": __victoryFrame,
    "Defeat": __defeatFrame
}

import pygame

from method_of_war.ui.persistent_ui.production_view import ProductionView
from method_of_war.ui.persistent_ui.top_action_bar_view import TopActionBarView
from method_of_war.ui.persistent_ui.troop_movements_view import *
from method_of_war.ui.persistent_ui.units_view import UnitsView


class PersistentViewManager:
    __mainWindow: pygame.display

    __topActionBarView: TopActionBarView
    __productionView: ProductionView
    __unitsView: UnitsView
    __troopMovementsView: TroopMovementsView

    def __init__(self, window):
        self.__mainWindow = window

        # setup persistent ui
        self.__topActionBarView = TopActionBarView(self.__mainWindow)
        self.__productionView = ProductionView(self.__mainWindow)
        self.__unitsView = UnitsView(self.__mainWindow)
        self.__troopMovementsView = TroopMovementsView(self.__mainWindow)

        # draw views
        self.__topActionBarView.drawView()
        self.__productionView.drawView()
        self.__unitsView.drawView()
        self.__troopMovementsView.drawView()

        # TEST SECTION START
        # test adding units
        unitsDict = {
            "Peon": 315,
            "Wyvern": 262,
            "Wolf Rider": 0,
            "War Kodo": 58,
            "a": 315,
            "aa": 262,
            "aaa": 12,
            "b": 58,
            "bb": 315,
            "bbb": 262,
            "c": 12
        }
        self.__unitsView.updateUnits(unitsDict)

        self.__productionView.updateProductionValues(5, 5, 5)

        self.__troopMovementsView.addElement(TroopMovementElement(AttackSize.BIG, True, "Orgrimmar", "Stormwind", 35))
        self.__troopMovementsView.addElement(TroopMovementElement(AttackSize.SMALL, False, "Stormwind", "Orgrimmar", 291))
        # TEST SECTION END

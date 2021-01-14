from method_of_war.core.enemy_core.enemy_settlement import EnemySettlement
from method_of_war.core.player_core.player_settlement import PlayerSettlement
from typing import List
from mini_engine.game_machine.a_mono_behaviour import MonoBehaviour
from method_of_war.ui import global_gameplay_view_manager
from method_of_war.core.levels import global_level
import pygame
import time


class GameResultControl(MonoBehaviour):
    __playerSettlement: PlayerSettlement
    __enemySettlements: List[EnemySettlement]

    __playerLost: bool = False
    __playerWon: bool = False

    __endLevelFunction = None

    def __init__(self, playerSettlement: PlayerSettlement, enemySettlements: List[EnemySettlement], endLevelFunction):
        super().__init__()
        self.__playerSettlement = playerSettlement
        self.__enemySettlements = enemySettlements
        self.__playerLost = False
        self.__playerWon = False
        self.__endLevelFunction = endLevelFunction

    def start(self):
        pass

    def update(self):
        pass

    def lateUpdate(self):
        if not self.__playerLost:
            if self.__playerSettlement.getSettlementDestruction().getIsDestroyed():
                self.__endLevelFunction()
                # display player lost screen
                global_level.levelIsActive = False
                # pygame.time.delay(200)
                # global_level.lateFunctionQueuedUp = True
                # global_level.lateFunction = global_gameplay_view_manager.globalGameplayViewManager.setDefeatScreen
                # time.sleep(0.1)
                global_gameplay_view_manager.globalGameplayViewManager.setDefeatScreen()
                self.__playerLost = True
        if not self.__playerWon:
            allEnemiesDestroyed: bool = True
            for enemySettlement in self.__enemySettlements:
                if not enemySettlement.getSettlementDestruction().getIsDestroyed():
                    allEnemiesDestroyed = False
            if allEnemiesDestroyed:
                self.__endLevelFunction()
                # display player won screen
                global_level.levelIsActive = False
                # pygame.time.delay(200)
                # global_level.lateFunctionQueuedUp = True
                # global_level.lateFunction = global_gameplay_view_manager.globalGameplayViewManager.setVictoryScreen
                # time.sleep(0.1)
                global_gameplay_view_manager.globalGameplayViewManager.setVictoryScreen()
                self.__playerWon = True

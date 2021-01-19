import time

from method_of_war.core.game_timer import GameTimer
from method_of_war.core.levels.game_level_1 import *
from method_of_war.ui import global_gameplay_view_manager
from method_of_war.ui import global_persistent_view_manager
from method_of_war.ui.ui_managers.gameplay_view_manager import *
from method_of_war.ui.ui_managers.persistent_view_manager import *

pygame.init()

# setup font
pygame.font.init()

mainWindow = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Method of War")
pygame.display.set_icon(gameIcon)

# setup ui
mainWindow.fill((0, 0, 0))
global_persistent_view_manager.globalPersistentViewManager = PersistentViewManager(mainWindow)
global_gameplay_view_manager.globalGameplayViewManager = GameplayViewManager(mainWindow)

# setup gameplay
gameTimer = GameTimer()
gameRealTime: float = 0
realTimeStartingSeconds: float = time.time()

# playersSettlement = PlayerSettlement()
level_1 = GameLevel1()
level_1.setupGameLevel()

global_level.levelIsActive = True
global_level.levelIsRunning = True
global_level.lateFunctionQueuedUp = False

while global_level.levelIsRunning:
    pygame.time.delay(tickMs)
    if global_level.levelIsActive:
        gameMachine.onTick()

        # manage real time
        gameMachine.onRealTime(gameRealTime)
        gameRealTime = (time.time() - realTimeStartingSeconds)

    # manage events
    for event in pygame.event.get():
        gameMachine.onEvent(event)
        if event.type == pygame.QUIT:
            global_level.levelIsRunning = False

    if global_level.levelIsActive:
        gameMachine.onLateTick()

    global_level.executeLateFunction()
    pygame.display.update()

pygame.quit()

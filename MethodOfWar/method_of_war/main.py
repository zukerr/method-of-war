from method_of_war.core.player_core.player_settlement import *
from method_of_war.ui.ui_managers.gameplay_view_manager import *
from method_of_war.ui.ui_managers.persistent_view_manager import *
from method_of_war.ui import global_gameplay_view_manager
from method_of_war.ui import global_persistent_view_manager
from method_of_war.core.game_timer import GameTimer
import time

pygame.init()

# setup font
pygame.font.init()

mainWindow = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Method of War")

# setup ui
mainWindow.fill((0, 0, 0))
global_persistent_view_manager.globalPersistentViewManager = PersistentViewManager(mainWindow)
global_gameplay_view_manager.globalGameplayViewManager = GameplayViewManager(mainWindow)

# setup gameplay
gameTimer = GameTimer()
gameRealTime: float = 0
realTimeStartingSeconds: float = time.time()

playersSettlement = PlayerSettlement()

run = True
while run:
    pygame.time.delay(tickMs)
    gameMachine.onTick()

    # manage real time
    gameMachine.onRealTime(gameRealTime)
    gameRealTime = (time.time() - realTimeStartingSeconds)

    # manage events
    for event in pygame.event.get():
        gameMachine.onEvent(event)
        if event.type == pygame.QUIT:
            run = False

    # pygame.draw.rect(mainWindow, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

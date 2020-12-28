from method_of_war.settlement import *
from method_of_war.ui.ui_managers.gameplay_view_manager import *
from method_of_war.ui.ui_managers.persistent_view_manager import *
from method_of_war.ui import global_gameplay_view_manager

pygame.init()

# setup font
pygame.font.init()

mainWindow = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Method of War")

# setup ui
mainWindow.fill((0, 0, 0))
persistentViewManager = PersistentViewManager(mainWindow)
global_gameplay_view_manager.globalGameplayViewManager = GameplayViewManager(mainWindow)

run = True
while run:
    pygame.time.delay(tickMs)
    gameMachine.onTick()

    for event in pygame.event.get():
        gameMachine.onEvent(event)
        if event.type == pygame.QUIT:
            run = False

    # pygame.draw.rect(mainWindow, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

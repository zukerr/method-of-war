from mini_engine.game_machine.game_machine_main import *

# for 62.5 fps, tickMs = 16
tickMs: int = 16
gameMachine: GameMachine = GameMachine()


def getFpsCount():
    return 1000 / tickMs

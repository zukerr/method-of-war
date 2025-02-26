from abc import *

from method_of_war.ui.ui_global import *


class View(ABC):
    _window: pygame.display

    def __init__(self, window):
        self._window = window

    @abstractmethod
    def drawView(self):
        pass

    def disableView(self):
        pass

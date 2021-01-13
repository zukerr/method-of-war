from method_of_war.ui.menu_ui.a_game_result_view import GameResultView


class DefeatView(GameResultView):
    def __init__(self, window):
        super().__init__(window, gameResultStr="Defeat", gameResultCaps="DEFEAT", gameResultTextX=470)

from method_of_war.ui.menu_ui.a_game_result_view import GameResultView


class VictoryView(GameResultView):
    def __init__(self, window):
        super().__init__(window, gameResultStr="Victory", gameResultCaps="VICTORY", gameResultTextX=438)

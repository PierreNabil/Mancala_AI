from .human_player import Player
from ..minimax import minimax_alpha_beta

MAX_DEPTH = 5

class AIPlayer(Player):
    def __init__(self, player_id):
        self.player_id = player_id

    def move(self, state):
        move, value = minimax_alpha_beta(state, MAX_DEPTH)

        print()
        print(f"Board Value: {value}. Move: {move}")

        new_state = state.make_move(move)
        return new_state
from .human_player import Player
from ..minimax import minimax_alpha_beta

class AIPlayer(Player):
    def __init__(self, player_id, dificulty):
        self.player_id = player_id
        self.max_depth = 2 * dificulty - 1

    def move(self, state):
        move, value = minimax_alpha_beta(state, self.max_depth)

        printed_move = move-7 if self.player_id==1 else move

        print()
        print(f"Board Value: {value}. Move: {printed_move}")

        new_state = state.make_move(move)
        return new_state
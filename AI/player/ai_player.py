from .human_player import Player
from ..minimax import minimax

MAX_DEPTH = 3

class AIPlayer(Player):
    def __init__(self, player_id):
        self.player_id = player_id

    def move(self, state):
        move, value = minimax(state, MAX_DEPTH)
        
        print()
        print("Board Value:" , value)

        new_state = state.make_move(move)
        return new_state
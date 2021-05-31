from ..errors import InvalidMoveError

class Player:
    pass

class HumanPlayer(Player):
    def __init__(self, player_id):
        self.player_id = player_id

    def move(self, state):
        move = None
        print()
        while move not in state.possible_moves():
            move = int(input("Enter move [0,5]: "))

            if self.player_id == 1:
                move = move + 7

        new_state = state.make_move(move)
        return new_state
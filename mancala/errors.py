class MancalaError(Exception):
    pass

class InvalidMoveError(MancalaError):
    def __init__(self, given_move, game_state):
        self.given_move = given_move
        self.possible_moves = list(game_state.possible_moves())

    def __str__(self):
        return "Move {} is invalid. Try one of {}.".format(self.given_move, self.possible_moves)
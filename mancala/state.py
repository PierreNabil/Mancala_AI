from copy import deepcopy

START_STATE = ([4]*6 + [0])*2

class GameState:
    def __init__(self, init_state=START_STATE):
        if isinstance(init_state, GameState):
            self = init_state
        else:
            self.state = init_state
            self.player_turn = 0

    def show(self):
        print()
        print("Player {}'s turn:".format(self.player_turn))
        print("      5   4   3   2   1   0")
        print("[{:2}]({:2})({:2})({:2})({:2})({:2})({:2})[  ]".format(*self.state[7:][::-1]))
        print("[  ]({:2})({:2})({:2})({:2})({:2})({:2})[{:2}]".format(*self.state[:7]))
        print("      0   1   2   3   4   5")

    def is_terminal(self):
        player_0_win = sum(self.state[0:6]) == 0
        player_1_win = sum(self.state[7:13]) == 0

        if  player_0_win or player_1_win:
            return True
        return False

    def children(self):
        for move in self.possible_moves():
            new_state = self.make_move(move)
            yield new_state

    def possible_moves(self):
        if self.player_turn == 0:
            for i in range(6):
                if self.state[i] != 0:
                    yield i
        else:
            for i in range(7,13):
                if self.state[i] != 0:
                    yield i
            
    def make_move(self, move):
        # assumes that the move is valid
        new_state = deep_copy(self.state)
        hand = new_state[move]
        new_state[move] = 0

        while hand > 0:
            move = (move + 1) % 14
            hand -= 1
            new_state[move] += 1

        next_player = 1- self.player_turn
        return GameState(new_state, next_player)



if __name__ == "__main__":
    state = GameState()
    state.show()
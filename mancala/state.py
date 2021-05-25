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
        print("[{:2}]({:2})({:2})({:2})({:2})({:2})({:2})[  ]".format(*self.state[7::-1]))
        print("[  ]({:2})({:2})({:2})({:2})({:2})({:2})[{:2}]".format(*self.state[:7]))

    def is_terminal(self):
        #TODO:
        pass

    def children(self):
        #TODO: Iterator on child_nodes
        pass


if __name__ == "__main__":
    state = GameState()
    state.show()
from copy import deepcopy

START_STATE = ([4]*6 + [0])*2


class PocketName:
    num_pockets = 14

    p0_mancala = 6
    p1_mancala = 13

    p0_pockets = list(range(6))
    p1_pockets = list(range(12,6,-1))


class GameState:
    def __init__(self, init_state=START_STATE, player_turn=0, stealing=True):
        self.state = init_state
        self.player_turn = player_turn
        self.stealing = stealing
        self.winner = None

    def show(self):
        print()
        print("Player {}'s turn:".format(self.player_turn))
        print("      5   4   3   2   1   0")
        print("[{:2}]({:2})({:2})({:2})({:2})({:2})({:2})[  ]".format(*self.state[-1:6:-1]))
        print("[  ]({:2})({:2})({:2})({:2})({:2})({:2})[{:2}]".format(*self.state[:7]))
        print("      0   1   2   3   4   5")

    def show_winning_message(self):
        print(f"Player {self.winner} Won!")

    def is_terminal(self):
        if self.winner is not None:
            return True
        return False

    def children(self):
        for move in self.possible_moves():
            new_state = self.make_move(move)
            yield move, new_state

    def possible_moves(self):
        if self.player_turn == 0:
            for i in PocketName.p0_pockets:
                if self.state[i] != 0:
                    yield i
        else:
            for i in PocketName.p1_pockets:
                if self.state[i] != 0:
                    yield i
            
    def make_move(self, move):
        # assumes that the move is valid
        player0_turn = self.player_turn == 0

        new_state = deepcopy(self.state)
        hand = new_state[move]
        new_state[move] = 0

        while hand > 0:
            move = (move + 1) % PocketName.num_pockets
            if (player0_turn and move == PocketName.p1_mancala) or (not player0_turn and move == PocketName.p0_mancala):
                # skip opponent's mancala
                continue
            hand -= 1
            new_state[move] += 1

        if self.stealing:
            if (player0_turn and move in PocketName.p0_pockets) or (not player0_turn and move in PocketName.p1_pockets):
                if new_state[move] == 1:
                    # steal marbles from opposite pocket if your pocket was empty
                    opposite_move = 12 - move
                    hand = new_state[move] + new_state[opposite_move]
                    new_state[move], new_state[opposite_move] = 0, 0

                    if player0_turn: new_state[PocketName.p0_mancala] += hand
                    else: new_state[PocketName.p1_mancala] += hand

        if (player0_turn and move == PocketName.p0_mancala) or (not player0_turn and move == PocketName.p1_mancala):
            # play again if last peice is put in your own mancala
            next_player = self.player_turn
        else:
            next_player = 1 - self.player_turn

        # check for winner
        game_done = sum(new_state[:6]) == 0 or sum(new_state[7:13]) == 0
        winner = None
        if game_done:
            if sum(new_state[:6]) == 0:
                new_state[PocketName.p1_mancala] += sum(new_state[7:13])
                for i in PocketName.p1_pockets:
                    new_state[i] = 0
            elif sum(new_state[7:13]) == 0:
                new_state[PocketName.p0_mancala] += sum(new_state[:6])
                for i in PocketName.p0_pockets:
                    new_state[i] = 0
            winner = 0 if new_state[PocketName.p0_mancala] > new_state[PocketName.p1_mancala] else 1

        new_game_state = GameState(new_state, next_player, self.stealing)
        new_game_state.winner = winner
        return new_game_state


if __name__ == "__main__":
    game_state = GameState()
    print(game_state.state)
    game_state.show()
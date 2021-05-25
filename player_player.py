from mancala import GameState, HumanPlayer

def player_player_game():
    game_state = GameState()
    player_0 = HumanPlayer(0)
    player_1 = HumanPlayer(1)

    while not game_state.is_terminal():
        game_state.show()
        if game_state.player_turn == 0:
            game_state = player_0.move(game_state)
        else:
            game_state = player_1.move(game_state)
    game_state.show_winning_message()


if __name__ == "__main__":
    player_player_game()
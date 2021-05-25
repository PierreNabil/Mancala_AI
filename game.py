from mancala import GameState
from AI import HumanPlayer, AIPlayer

default_ai_dificulty = 6

def player_player_game():
    player_0 = HumanPlayer(0)
    player_1 = HumanPlayer(1)
    play_game(player_0, player_1)

def player_ai_game(ai_difficulty):
    player_0 = HumanPlayer(0)
    player_1 = AIPlayer(1, ai_difficulty)
    play_game(player_0, player_1)

def ai_player_game(ai_difficulty):
    player_0 = AIPlayer(0, ai_difficulty)
    player_1 = HumanPlayer(1)
    play_game(player_0, player_1)

def ai_ai_game(ai0_difficulty, ai1_difficulty):
    player_0 = AIPlayer(0, ai0_difficulty)
    player_1 = AIPlayer(1, ai1_difficulty)
    play_game(player_0, player_1)



def play_game(player_0, player_1, stealing_mode=True):
    game_state = GameState(stealing=stealing_mode)

    while not game_state.is_terminal():
        game_state.show()
        if game_state.player_turn == 0:
            game_state = player_0.move(game_state)
        else:
            game_state = player_1.move(game_state)
    game_state.show()
    game_state.show_winning_message()



if __name__ == "__main__":
    # player_player_game()
    ai_ai_game(default_ai_dificulty, default_ai_dificulty)
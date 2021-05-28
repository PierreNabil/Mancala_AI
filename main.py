from game import play_game
from AI import HumanPlayer, AIPlayer

def main():
    print("Welcome to Mancala AI!")

    print()
    print("Please select player type: Human(h) or AI(a)")

    p0 = input("Player 0: ").strip().lower()
    if p0 == 'a':
        p0_diff = int(input("Dificulty level: "))

    p1 = input("Player 1: ").strip().lower()
    if p1 == 'a':
        p1_diff = int(input("Dificulty level: "))

    print()
    stealing_mode = input("Do you want stealing mode on? (y/n) ").strip().lower() == 'y'

    player_0 = HumanPlayer(0) if p0 != 'a' else AIPlayer(0, p0_diff)
    player_1 = HumanPlayer(1) if p1 != 'a' else AIPlayer(1, p1_diff)

    print()
    print("Let's play!")
    play_game(player_0, player_1, stealing_mode)
    # Press Enter to stop the game
    input()


if __name__ == "__main__":
    main()
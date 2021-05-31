# 4th_CSE_AI_Project
An AI to play the game Mancala designed from scratch.

## Contents

 - [Project Description](#Project-Description)
 - [Usage](#Usage)
 - [Team Members](#Team-Members)
 - [Features](#Features)


## Project Description
Mancala AI is a simple project where 2 players can play Mancala.
Both players can be either human players or AI with various levels of difficulty.

The game rules are as explained in [this video](https://www.youtube.com/watch?v=OX7rj93m6o8)
and it has 2 modes:
 - With Stealing
 - Without Stealing

The Game and its AI are implemented entirely from scratch in python.
The AI uses [minimax](https://en.wikipedia.org/wiki/Minimax)
with [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
where the depth of the tree search is given by this formula:

`depth = 2 * difficulty_level - 1`


## Usage

Here's a YouTube [video](https://www.youtube.com/watch?v=9p3riPJWUNw) that shows our game in action!

The simplest way to use Mancala AI is to run the [binary executable](/dist/mancala/mancala.exe) in `/dist/mancala/mancala.exe`.

You can also run the game by running [main.py](/main.py) using python.

Firstly, you'll have to select what type of player do you want player0 to be (either Human `h` or an AI `a`)
If an AI was selected, you'll have to select a difficulty level for the AI. 
A good difficulty level to start with is level 5 as it's fast enough to play without any significant delay but is still not too stupid as to not make the game fun. 
If the AI is too hard for you you can always select a lower difficulty and vice versa.

Repeat for the other player (player1).

Finally, you can select whether you want stealing mode on or off.


You'll find can also use one of the functions given in [game.py](/game.py) to skip the UI part of the project.


After selecting the 2 players of the game, the start board state is shown, and the game begins.
To enter a move, you can press a number between 0 and 5 which represents the pocket that you will take marbles from.
The rest of the rules are applied automatically.

Note that the pockets are numbered on the screen for both players so it should be easy for you to select the move you are looking for.


The game continues for each player until the end state is reached, where all extra marbles are relocated to their respective mancala and the final score for both players is calculated.
The Winner of the game is then declared and the game ends.


## Team Members

- [Pierre Nabil](https://github.com/PierreNabil)
- [Michael Magdy](https://github.com/Michael-M-Mike)
- [Christine Magdy](https://github.com/ChristineMagdy99)
- [John Bahaa](https://github.com/John-Bahaa)
- [Adham Nour]()


## Features

- An intuitive user interface for ease of use.
- A binary executable to run on any device without the need to be able to run python code.
- A DFS implementation of minimax and minimax with alpha-beta pruning that can be easilly used for other games.
- 2 Game Modes
  - With Stealing
  - Without Stealing
- Support of various difficulty levels corresponding to different game tree depths. (bonus feature #2)
- Support a networking mode where 2 instances of an AI player can play the game against each other without any human intervention. (bonus feature #5)
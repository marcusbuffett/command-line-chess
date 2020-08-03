[![Run on Repl.it](https://repl.it/badge/github/marcusbuffett/command-line-chess)](https://repl.it/github/marcusbuffett/command-line-chess)
command-line-chess
==================

A python program to play chess against an AI in the terminal.

## Installation

Requires Python 3, run the following to install :
  
    pip3 install cl-chess

## Usage

Run the following command after installation
  
    chess

Type '?' to get help at any time during the game.

You'll be asked to choose between playing as white or black, and what depth you want the AI to search :

![Initial](http://i.imgur.com/PSS7csc.png)

You can then make any (legal) move :

![First move](http://i.imgur.com/AsXhhvC.png)

## Options

Instead of a move, you can input :

* `l` to see every legal move
* `r` to make a random move
* `u` to undo your last move

## Technical stuff

The AI is a simple brute-force AI with no pruning. It evaluates a given position by counting the value of the pieces for each side (pawn -> 1, knight/bishop -> 3, rook -> 5, queen -> 9). It will evaluate the tree of moves, and take the path that results in the greatest gain. To learn more, check out [my post on how it works](https://mbuffett.com/posts/chess-ai/).

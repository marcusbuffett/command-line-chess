[![Run on Repl.it](https://repl.it/badge/github/marcusbuffett/command-line-chess)](https://repl.it/github/marcusbuffett/command-line-chess)

# command-line-chess

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/marcusbuffett/command-line-chess/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![PyPI download month](https://img.shields.io/pypi/dm/cl-chess.svg)](https://pypi.python.org/project/cl-chess/)
[![PyPi version](https://badgen.net/pypi/v/cl-chess/)](https://pypi.org/project/cl-chess)
[![GitHub issues](https://img.shields.io/github/issues/marcusbuffett/command-line-chess.svg)](https://GitHub.com/marcusbuffett/command-line-chess/issues/)
[![GitHub watchers](https://img.shields.io/github/watchers/marcusbuffett/command-line-chess.svg?style=social&label=Watch&maxAge=2592000)](https://github.com/marcusbuffett/command-line-chess)
[![GitHub stars](https://img.shields.io/github/stars/marcusbuffett/command-line-chess.svg?style=social&label=Star&maxAge=2592000)](https://github.com/marcusbuffett/command-line-chess)


A python program to play chess against an AI in the terminal.

Also check out my other project, a [chess training site](https://chessmadra.com/).

## Features

- Play chess against an AI in the terminal
- Two player mode (run `chess --two` to enter)
- possible commands:
    * `a3`, `Nc3`, `Qxa`, etc: make a move
    * `l`: prints every legal move
    * `r`: make a random move
    * `u`: undo your last move
    * `quit`: resign the current game
    * `gm`: prints moves of current game in PGN format
    * `?`: help, prints all available commands

## Screenshots
Initial State:

![Initial](https://i.imgur.com/PSS7csc.png)

First move:

![First move](https://i.imgur.com/AsXhhvC.png)

## Installation

### Install from [PyPI](https://pypi.org/project/cl-chess/)
Just run the following command:

```
pip install cl-chess
```

### Install from source
- First clone the repository:
```
git clone https://github.com/marcusbuffett/command-line-chess
```
- navigate into the newly created `command-line-chess` directory and run:
```
pip install .
```
## Usage

```sh
chess -h        # to see all possible options
```
```
usage: chess [-h] [-t] [-w W] [-b B] [-c]

A python program to play chess against an AI in the terminal.

optional arguments:
  -h, --help       show this help message and exit
  -t, --two        to play a 2-player game (default: False)
  -w W, --white W  color for white player (default: white)
  -b B, --black B  color for black player (default: black)
  -c, --checkered  use checkered theme for the chess board (default: False)

Enjoy the game!

```

## Contributing

Contributions are always welcome!

See `CONTRIBUTING.md`for ways to get started.

Please adhere to this project's `CODE-OF-CONDUCT.md`.


## LICENSE
Take a look at the [LICENSE](https://github.com/marcusbuffett/command-line-chess/LICENSE) file

## Authors

- [@marcusbuffett](https://www.github.com/marcusbuffett)
- [@ClasherKasten](https://www.github.com/ClasherKasten)


## Questions, bugs, etc.
Please create an issue.

## Technical stuff

The AI is a simple brute-force AI with no pruning. It evaluates a given position by counting the value of the pieces for each side (pawn -> 1, knight/bishop -> 3, rook -> 5, queen -> 9). It will evaluate the tree of moves, and take the path that results in the greatest gain. To learn more, check out [my post on how it works](https://mbuffett.com/posts/chess-ai/).

# chesslib

## Getting started

### Installation

In your project folder create a new virtual environment, unless you already have one, and source it:
```
python3 -m venv env
source env/bin/activate
```
Clone the repository and install it using pip:
```
git clone https://github.com/DanielH4/chesslib
pip install ./chesslib
```
The library should now be installed and the cloned repository can be removed if
you don't wish to use if for the actions listed below.

### Playing chess

The project repository contains a `main.py` file which may be run to play a game of
chess on the terminal. 
```
cd chesslib/
python main.py
```
Square input is given as `a1` for example. The main file may also serve as an example 
of how the library can be used.

### Running tests

If the repository has been cloned and installed, then tests can be run using:
```
cd chesslib/
python -m pytest
```


## Usage

The library's functionality is primarily exposed through the `Chess` class 
found in `chesslib.api`, which can be used with the following import:

`from chesslib.api import Chess`.

### Properties

The properties of a `Chess` object are shown in the following code snippet:
```
chess = Chess()
print(chess.turn)
print(chess.check)
print(chess.checkmate)
```
Output:
```
white
False
False
```

### Moving a piece

A piece may be moved with the `move` method:
```
chess = Chess()
chess.move('e2', 'e4')
```
where the squares are given as their textual representations. A move will return
`None` if the move is not valid. A move is only valid if the current player can play it.


### Inspecting legal moves

The method `legal_moves` will return a set of tuples representing legal moves of 
a given color in the current board state. The first element of a tuple is the square
being moved from and the second element the square being moved to.
```
chess = Chess()
print(chess.legal_moves(color='white'))
```
Output:
```
{('a2', 'a3'), ('g1', 'h3'), ('e2', 'e4'), ('d2', 'd4'), ('a2', 'a4'), ('h2', 'h4'),
('h2', 'h3'), ('c2', 'c4'), ('b2', 'b3'), ('d2', 'd3'), ('b1', 'c3'), ('b2', 'b4'),
('c2', 'c3'), ('g1', 'f3'), ('f2', 'f3'), ('f2', 'f4'), ('e2', 'e3'), ('g2', 'g3'), 
('b1', 'a3'), ('g2', 'g4')}
```

### Printing state

```
chess = Chess()
chess.print()
```
Output:
```
Turn: white
Check: False
rnbqkbnr
pppppppp
........
........
........
........
PPPPPPPP
RNBQKBNR
```

### JSON serialization and deserialization

The method `toJSON` allows us to convert a `Chess` object to a JSON formatted string.
The optional argument `prettify` inserts whitespace to produce a more readable string.
```
chess = Chess()
json_str = chess.toJSON(prettify=True)
print(json_str)
```
Output:
```
{
  "board": {
    "board": [
      {
        "type": "rook",
        "color": "white",
        "value": 5,
        "has_moved": false
      },
      {
        "type": "knight",
        "color": "white",
        "value": 3
      },
      {
        "type": "bishop",
        "color": "white",
        "value": 3
      },
      {
        "type": "queen",
        "color": "white",
        "value": 9
      },
      {
        "type": "king",
        "color": "white",
        "value": null,
        "has_moved": false
      },
      {
        "type": "bishop",
        "color": "white",
        "value": 3
      },
      {
        "type": "knight",
        "color": "white",
        "value": 3
      },
      {
        "type": "rook",
        "color": "white",
        "value": 5,
        "has_moved": false
      },
      {
        "type": "pawn",
        "color": "white",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "white",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "white",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "white",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "white",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "white",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "white",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "white",
        "value": 1,
        "en_passantable": false
      },
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      {
        "type": "pawn",
        "color": "black",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "black",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "black",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "black",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "black",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "black",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "black",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "pawn",
        "color": "black",
        "value": 1,
        "en_passantable": false
      },
      {
        "type": "rook",
        "color": "black",
        "value": 5,
        "has_moved": false
      },
      {
        "type": "knight",
        "color": "black",
        "value": 3
      },
      {
        "type": "bishop",
        "color": "black",
        "value": 3
      },
      {
        "type": "queen",
        "color": "black",
        "value": 9
      },
      {
        "type": "king",
        "color": "black",
        "value": null,
        "has_moved": false
      },
      {
        "type": "bishop",
        "color": "black",
        "value": 3
      },
      {
        "type": "knight",
        "color": "black",
        "value": 3
      },
      {
        "type": "rook",
        "color": "black",
        "value": 5,
        "has_moved": false
      }
    ]
  },
  "turn": "white",
  "check": false,
  "checkmate": false
}
```

Similarly, the static method `fromJSON` takes a json formatted string with a required
format similar to the above output and returns a `Chess` object. 

Example usage:
```
chess = Chess.fromJSON(json_str)
```
given that `json_str` is properly formatted.


The json property `value` for pieces is not required but the other properties are 
as they fully detail the state of the game. Notice that rooks, kings, and pawns have 
additional required properties compared to other pieces. For instance, the pawn property
`en_passantable` should only be set to `True` if it was moved two squares forward in the
previous turn. The `has_moved` property for kings and rooks remains `True` for the remainder
of the game if it has moved once.

from chesslib.bishop import Bishop


def create_default_board():
    return [None] * 64


# converts a square string (e.g. 'b4') to the respective array index
def square_to_index(square):
    column = ord(square[0]) - 97
    row = int(square[1]) - 1
    return (row * 8) + column


# converts an array index to the respective square string (e.g. 'b4')
def index_to_square(index):
    row = str(int(index / 8) + 1)
    column = chr(97 + (index % 8))
    return f"{column}{row}"


class ChessBoard():
    def __init__(self):
        self._board = create_default_board()

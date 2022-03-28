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


# returns a set of the squares in the column of a given square
def get_board_column(square):
    column_index = square_to_index(square) % 8
    return {index_to_square(column_index + (row_index * 8)) for row_index in range(8)}


# returns a set of squares in the row of a given square
def get_board_row(square):
    row_index = int(square_to_index(square) / 8)
    return {index_to_square(column_index + (row_index * 8)) for column_index in range(8)}


class ChessBoard():
    def __init__(self):
        self._board = create_default_board()

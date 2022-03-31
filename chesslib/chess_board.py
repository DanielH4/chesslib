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


# returns true if a square moved x,y amount in rows and columns 
# relative to a given square index is still within the bounds of the board
def is_in_board(square_index, row_change=0, col_change=0):
    row_index = int(square_index / 8)
    col_index = square_index % 8
    in_row_bounds = in_col_bounds = False

    if row_index + row_change >= 0 and row_index + row_change < 8:
        in_row_bounds = True

    if col_index + col_change >= 0 and col_index + col_change < 8:
        in_col_bounds = True

    return (in_row_bounds and in_col_bounds)


def get_surrounding_squares(square):
    square_index = square_to_index(square)

    surrounding_squares = set()
    for row_offset in range(-1, 1+1):
        for col_offset in range(-1, 1+1):
            if is_in_board(square_index, row_offset, col_offset):
                surrounding_square_index = square_index + col_offset + (8 * row_offset)
                surrounding_squares.add(index_to_square(surrounding_square_index))

    return surrounding_squares


class ChessBoard():
    def __init__(self):
        self._board = create_default_board()

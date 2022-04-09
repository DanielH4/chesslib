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


# returns the set of squares in a row from the given square until encountering a piece
def get_board_row(board, square):
    square_index = square_to_index(square)

    row_squares = set()

    for direction in (-1,1):
        for col_offset in range(1,8):
            if not is_in_board(square_index, 0, col_offset * direction):
                break

            offset_square = index_to_square(square_index + (col_offset * direction))

            row_squares.add(offset_square)

            if not board.is_empty_square(square):
                break

    return row_squares


# returns the set of squares diagonal from the given square until encountering a piece
def get_board_diagonals(board, square):
    square_index = square_to_index(square)

    diagonal_squares = set()

    # possibly 4 diagonal directions from given square
    for diagonal in ((1,1), (1,-1), (-1,1), (-1,-1)):
        for offset in range(1,8):
            row_offset = offset * diagonal[0]
            col_offset = offset * diagonal[1]
            offset_square = index_to_square(square_index + col_offset + (8 * row_offset))

            if is_in_board(square_index, row_offset, col_offset):
                diagonal_squares.add(offset_square)

                # stop diagonal traversal if a piece is encountered
                is_occupied_square = board.get_piece(offset_square) is not None
                if is_occupied_square:
                    break

    return diagonal_squares


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

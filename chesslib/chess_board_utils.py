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


# returns the set of squares in a column from the given square until encountering a piece
def get_board_column(board, square):
    square_index = square_to_index(square)

    col_squares = set()

    for direction in (-1,1):
        for row_offset in range(1,8):
            if not is_in_board(square_index, row_offset * direction, 0):
                break

            offset_square = index_to_square(square_index + (8 * (row_offset * direction)))

            col_squares.add(offset_square)

            if not board.is_empty_square(offset_square):
                break

    return col_squares


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

            if not board.is_empty_square(offset_square):
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
                if not board.is_empty_square(offset_square):
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


# returns a set of up to n squares in front of the given square
# 'front' is determined by color (opposite of starting side of the board)
# includes squares where a piece is encountered but stops iteration early
def get_n_front_squares(board, square, color, n):
    square_index = square_to_index(square)

    front_squares = set()

    row_offsets = range(1,n+1) if color == 'white' else range(-1,-n-1,-1)
    for row_offset in row_offsets:
        if not is_in_board(square_index, row_change=row_offset):
            break

        offset_square = index_to_square(square_index + (8 * row_offset))
        front_squares.add(offset_square)

        if not board.is_empty_square(offset_square):
            break

    return front_squares


# returns the two diagonal squares in front of the given square as a set
def get_front_diagonal_squares(square, color):
    square_index = square_to_index(square)
    diagonal_offsets = ((1,1), (1,-1)) if color == 'white' else ((-1,1), (-1,-1))

    front_diagonal_squares = set()
    for offsets in diagonal_offsets:
        row_offset = offsets[0]
        col_offset = offsets[1]
        if is_in_board(square_index, row_offset, col_offset):
            diagonal_square = index_to_square(square_index + col_offset + (8 * row_offset))
            front_diagonal_squares.add(diagonal_square)

    return front_diagonal_squares

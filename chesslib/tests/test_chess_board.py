from chesslib.chess_board import *


def test_square_to_index():
    assert (
        square_to_index('a1') == 0
        and
        square_to_index('h8') == 63
        and
        square_to_index('e5') == 36)


def test_index_to_square():
    assert (
        index_to_square(0) == 'a1'
        and
        index_to_square(63) == 'h8'
        and
        index_to_square(36) == 'e5')

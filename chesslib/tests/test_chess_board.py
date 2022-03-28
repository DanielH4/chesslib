from chesslib.chess_board import *


def test_square_to_index():
    assert (
        square_to_index('a1') == 0
        and
        square_to_index('h8') == 63
        and
        square_to_index('e5') == 36)

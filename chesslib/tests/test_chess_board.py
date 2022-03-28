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


def test_get_board_column():
    expected = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'}
    assert get_board_column('h4') == expected


def test_get_board_row():
    expected = {'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'}
    assert get_board_row('c3') == expected

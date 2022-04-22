from chesslib.chess_board_utils import *
from chesslib.chess_board import ChessBoard


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


def test_get_board_column_on_empty_board():
    expected = {'h1', 'h2', 'h3', 'h5', 'h6', 'h7', 'h8'}
    assert get_board_column(ChessBoard(), 'h4') == expected


def test_get_board_row_on_empty_board():
    expected = {'a3', 'b3', 'd3', 'e3', 'f3', 'g3', 'h3'}
    assert get_board_row(ChessBoard(), 'c3') == expected


def test_get_board_diagonals_on_empty_board():
    expected_e4 = {
        'a8', 'b7', 'c6', 'd5', 'f3', 'g2', 'h1',
        'b1', 'c2', 'd3', 'f5', 'g6', 'h7'
    }
    expected_b7 = {
        'a8', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1',
        'a6', 'c8'
    }
    assert (
        get_board_diagonals(ChessBoard(), 'e4') == expected_e4
        and
        get_board_diagonals(ChessBoard(), 'b7') == expected_b7)


def test_is_in_board():
    assert (
        is_in_board(square_to_index('a1'), -1, -1) == False
        and
        is_in_board(square_to_index('a8'), 0, -1) == False
        and
        is_in_board(square_to_index('h8'), 1, 0) == False
        and
        is_in_board(square_to_index('h1'), 0, 1) == False
        and
        is_in_board(square_to_index('h1'), 1, -1) == True)


def test_get_surrounding_squares():
    expected_a1 = {'a1', 'a2', 'b2', 'b1'}
    expected_h1 = {'h1', 'h2', 'g2', 'g1'}
    expected_a8 = {'a8', 'b8', 'b7', 'a7'}
    expected_h8 = {'h8', 'g8', 'g7', 'h7'}
    assert (
        get_surrounding_squares('a1') == expected_a1
        and
        get_surrounding_squares('h1') == expected_h1
        and
        get_surrounding_squares('a8') == expected_a8
        and
        get_surrounding_squares('h8') == expected_h8)


def test_get_n_front_squares():
    assert (
        get_n_front_squares(ChessBoard(), 'd4', 'white', 1) == {'d5'}
        and
        get_n_front_squares(ChessBoard(), 'd4', 'black', 2) == {'d3', 'd2'})


def test_get_front_diagonal_squares():
    assert(
        get_front_diagonal_squares('d4', 'white') == {'c5', 'e5'}
        and
        get_front_diagonal_squares('d4', 'black') == {'c3', 'e3'})

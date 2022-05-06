import pytest

from chesslib.chess_board import *


def test_create_default_board():
    assert str(ChessBoard()) == ("RNBQKBNR\n"
                                 "PPPPPPPP\n"
                                 "........\n"
                                 "........\n"
                                 "........\n"
                                 "........\n"
                                 "pppppppp\n"
                                 "rnbqkbnr")


def test_create_board_from_str():
    with pytest.raises(InvalidBoardSizeError) as e_info:
        create_board_from_str("...")
    with pytest.raises(UnicodeDecodeError) as e_info:
        create_board_from_str("x......."
                              "........"
                              "........"
                              "........"
                              "........"
                              "........"
                              "........"
                              "........")


def test_set_square():
    square = 'a1'
    piece = Rook('white')
    board = ChessBoard()
    board.set_square(square, piece)
    assert board.get_piece(square) == piece


def test_get_pieces():
    default_board = ChessBoard()
    white_pieces = default_board.get_pieces('white')
    black_pieces = default_board.get_pieces('black')
    assert(
        len(default_board.get_pieces()) == 32
        and
        len(white_pieces) == 16
        and
        len(black_pieces) == 16
        and
        all([piece.color == 'white' for piece in white_pieces])
        and
        all([piece.color == 'black' for piece in black_pieces]))

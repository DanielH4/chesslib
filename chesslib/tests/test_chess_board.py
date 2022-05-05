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

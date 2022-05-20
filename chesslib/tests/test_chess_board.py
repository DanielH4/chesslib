import pytest

from chesslib.chess_board import *


def test_create_default_board():
    assert str(ChessBoard().to_string()) == ("rnbqkbnr"
                                             "pppppppp"
                                             "........"
                                             "........"
                                             "........"
                                             "........"
                                             "PPPPPPPP"
                                             "RNBQKBNR")


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


def test_get_position():
    board = ChessBoard("...R...."
                       "........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "........")
    square = 'd1'
    piece = board.get_piece(square)
    assert board.get_square(piece) == square


def test_to_string():
    assert (
        ChessBoard().to_string() == ("rnbqkbnr"
                                     "pppppppp"
                                     "........"
                                     "........"
                                     "........"
                                     "........"
                                     "PPPPPPPP"
                                     "RNBQKBNR")
        and
        ChessBoard().to_string(playing_color='black') == ("RNBKQBNR"
                                                          "PPPPPPPP"
                                                          "........"
                                                          "........"
                                                          "........"
                                                          "........"
                                                          "pppppppp"
                                                          "rnbkqbnr"))


def test_get_moves():
    board = ChessBoard("........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "Rn......")
    white_rook_moves = {
        ('a8', 'a7'),
        ('a8', 'a6'),
        ('a8', 'a5'),
        ('a8', 'a4'),
        ('a8', 'a3'),
        ('a8', 'a2'),
        ('a8', 'a1'),
        ('a8', 'b8')
    }
    black_knight_moves = {
        ('b8', 'a6'),
        ('b8', 'c6'),
        ('b8', 'd7')
    }

    assert (
        board.get_moves() == white_rook_moves | black_knight_moves
        and
        board.get_moves('white') == white_rook_moves
        and
        board.get_moves('black') == black_knight_moves
    )

def test_swap_pieces():
    board = ChessBoard("........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "Rn......")
    rook_square = 'a8'
    knight_square = 'b8'
    rook = board.get_piece(rook_square)
    knight = board.get_piece(knight_square)
    board.swap_pieces(rook_square, knight_square)
    assert (
        board.get_piece(rook_square) is knight
        and
        board.get_piece(knight_square) is rook
    )

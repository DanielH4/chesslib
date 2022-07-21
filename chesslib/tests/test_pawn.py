from chesslib.pawn import Pawn
from chesslib.chess_board import ChessBoard


def test_pawn_legal_moves_default_position_white():
    board = ChessBoard("........"
                       "P......."
                       "........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "........")
    square = 'a2'
    pawn = board.get_piece(square)
    assert pawn.legal_moves(board, square) == {'a3', 'a4'}


def test_pawn_legal_moves_default_position_black():
    board = ChessBoard("........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "p......."
                       "........")
    square = 'a7'
    pawn = board.get_piece(square)
    assert pawn.legal_moves(board, square) == {'a6', 'a5'}


def test_pawn_legal_moves_capture_white():
    board = ChessBoard("........"
                       "........"
                       "........"
                       "...P...."
                       "..pPp..."
                       "........"
                       "........"
                       "........")
    square = 'd4'
    pawn = board.get_piece(square)
    assert pawn.legal_moves(board, square) == {'c5', 'e5'}


def test_pawn_legal_moves_capture_black():
    board = ChessBoard("........"
                       "........"
                       "........"
                       "..PpP..."
                       "...p...."
                       "........"
                       "........"
                       "........")
    square = 'd5'
    pawn = board.get_piece(square)
    assert pawn.legal_moves(board, square) == {'c4', 'e4'}


def test_pawn_legal_diagonal_moves():
    board = ChessBoard("........"
                       "........"
                       "........"
                       ".....PpP"
                       "pPp....."
                       "........"
                       "........"
                       "........")
    board.get_piece('a5').en_passantable = True
    board.get_piece('c5').en_passantable = True
    board.get_piece('f4').en_passantable = True
    board.get_piece('h4').en_passantable = True
    white_pawn = board.get_piece('b5')
    black_pawn = board.get_piece('g4')
    assert (
        white_pawn._legal_diagonal_moves(board, 'b5') == {'a6', 'c6'}
        and
        black_pawn._legal_diagonal_moves(board, 'g4') == {'f3', 'h3'})


def test_pawn_legal_moves_custom_position_white():
    board = ChessBoard("........"
                       "........"
                       "........"
                       "........"
                       "...P...."
                       "........"
                       "........"
                       "........")
    square = 'd5'
    pawn = board.get_piece(square)
    assert pawn.legal_moves(board, square) == {'d6'}


def test_pawn_legal_moves_custom_position_black():
    board = ChessBoard("........"
                       "........"
                       "........"
                       "........"
                       "...p...."
                       "........"
                       "........"
                       "........")
    square = 'd5'
    pawn = board.get_piece(square)
    assert pawn.legal_moves(board, square) == {'d4'}

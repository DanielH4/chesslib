from chesslib.api import Chess
from chesslib.chess_board import ChessBoard


def test_legal_moves():
    game = Chess()
    game._board = ChessBoard("........"
                             "........"
                             "........"
                             "........"
                             "........"
                             "........"
                             "........"
                             "Rn......")
    white_rook_legal_moves = {
        ('a8', 'a7'),
        ('a8', 'a6'),
        ('a8', 'a5'),
        ('a8', 'a4'),
        ('a8', 'a3'),
        ('a8', 'a2'),
        ('a8', 'a1'),
        ('a8', 'b8')
    }
    black_knight_legal_moves = {
        ('b8', 'a6'),
        ('b8', 'c6'),
        ('b8', 'd7')
    }

    assert (
        game.legal_moves('white') == white_rook_legal_moves
        and
        game.legal_moves('black') == black_knight_legal_moves
    )


def test_move():
    game = Chess()
    game._board = ChessBoard("Q......."
                             "p......."
                             "........"
                             "........"
                             "........"
                             "........"
                             "........"
                             "........")
    moved_piece = game._board.get_piece('a1')
    captured_piece = game._board.get_piece('a2')
    game.move('a1', 'b1')
    assert (
        game._board.get_piece('a1') is None
        and
        game._board.get_piece('b1') is moved_piece
        and
        game.move('b1', 'a2') == captured_piece.value
        and
        Chess().move('a5', 'a4') is None # illegal move
    )

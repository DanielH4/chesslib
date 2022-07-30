from chesslib.king import King
from chesslib.chess_board import ChessBoard


def test_king_legal_moves():
    board = ChessBoard("........"
                       "........"
                       "........"
                       "....K..."
                       "...kK..."
                       "....KK.."
                       "........"
                       "........")
    square = 'e5'
    king = board.get_piece(square)
    assert king.legal_moves(board, square) == {'d4', 'f4', 'd5', 'f5', 'd6'}


def test_legal_castling_moves():
    board = ChessBoard("R..K...R"
                       "........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "........"
                       "r..k...r")
    white_king_square = 'd1'
    black_king_square = 'd8'
    white_king = board.get_piece(white_king_square)
    black_king = board.get_piece(black_king_square)
    black_king.has_moved = True
    board.get_piece('h1').has_moved = True
    assert ({'a1'}.issubset(white_king.legal_moves(board, white_king_square)) and
            black_king.legal_moves(board, black_king_square) == {'c8', 'e8', 'c7', 'd7', 'e7'})

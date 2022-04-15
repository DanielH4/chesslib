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

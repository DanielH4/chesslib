from chesslib.rook import Rook
from chesslib.chess_board import ChessBoard


def test_rook_legal_moves():
    board = ChessBoard("........"
                       ".r......"
                       "........"
                       "........"
                       "RR.....r"
                       ".R......"
                       "........"
                       "........")
    square = 'b5'
    rook = board.get_piece(square)
    assert rook.legal_moves(board, square) == {'b4', 'b3', 'b2', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'}

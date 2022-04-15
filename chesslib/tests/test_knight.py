from chesslib.knight import Knight
from chesslib.chess_board import ChessBoard


def test_knight_legal_moves():
    board = ChessBoard("........"
                       "........"
                       "........"
                       ".....n.."
                       "........"
                       "......N."
                       "....N..."
                       "........")
    square = 'g6'
    knight = board.get_piece(square)
    assert knight.legal_moves(board, square) == {'h4', 'f4', 'e5', 'f8', 'h8'}

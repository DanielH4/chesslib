from chesslib.bishop import Bishop
from chesslib.chess_board import ChessBoard


def test_bishop_legal_moves():
    board = ChessBoard("........"
                       ".....B.."
                       "..B....."
                       "...B...."
                       "..b.b..."
                       "........"
                       "........"
                       "........")
    square = 'd4'
    bishop = board.get_piece('d4')
    assert bishop.legal_moves(board, square) == {'e3', 'c5', 'e5'}

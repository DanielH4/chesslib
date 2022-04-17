from chesslib.queen import Queen
from chesslib.chess_board import ChessBoard


def test_queen_legal_moves():
    board = ChessBoard("........"
                       "........"
                       "q.q.q..."
                       "........"
                       "..q.q..."
                       "........"
                       "..q.Q..."
                       "........")
    square = 'c5'
    queen = board.get_piece(square)
    diag_squares = {'d4', 'b4', 'd6', 'e7', 'b6', 'a7'}
    row_squares = {'a5', 'b5', 'd5'}
    col_squares = {'c4', 'c6'}
    assert queen.legal_moves(board, square) == (diag_squares | row_squares | col_squares)

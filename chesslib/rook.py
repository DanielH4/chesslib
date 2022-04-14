from chesslib.piece import Piece
from chesslib.chess_board_utils import get_board_row, get_board_column


class Rook(Piece):
    def __init__(self, color):
        self._color = color
        self._value = 5

    def legal_moves(self, board, square):
        def is_legal_move(square):
            piece = board.get_piece(square)

            if board.is_empty_square(square) or piece.color != self.color:
                return True
            return False

        return set(filter(is_legal_move, get_board_row(board, square) 
                                         | get_board_column(board, square)))

    @staticmethod
    def white_ascii_representation():
        return 'R'

    @staticmethod
    def black_ascii_representation():
        return 'r'

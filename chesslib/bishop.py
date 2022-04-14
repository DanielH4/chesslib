from chesslib.piece import Piece
from chesslib.chess_board_utils import get_board_diagonals


class Bishop(Piece):
    def __init__(self, color):
        self._color = color
        self._value = 3

    def legal_moves(self, board, square):
        def is_legal_move(square):
            return self._is_legal_move(board, square)

        potential_moves = get_board_diagonals(board, square)
        return set(filter(is_legal_move, potential_moves))

    @staticmethod
    def white_ascii_representation():
        return 'B'

    @staticmethod
    def black_ascii_representation():
        return 'b'

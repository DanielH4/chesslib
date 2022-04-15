from chesslib.piece import Piece
from chesslib.chess_board_utils import get_surrounding_squares


class King(Piece):
    def __init__(self, color):
        self._color = color
        self._value = None

    def legal_moves(self, board, square):
        def is_legal_move(square):
            return self._is_legal_move(board, square)

        return set(filter(is_legal_move, get_surrounding_squares(square)))

    @staticmethod
    def white_ascii_representation():
        return 'K'

    @staticmethod
    def black_ascii_representation():
        return 'k'

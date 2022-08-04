from chesslib.piece import Piece
from chesslib.chess_board_utils import get_board_row, get_board_column


class Rook(Piece):
    def __init__(self, color):
        self._type = 'rook'
        self._color = color
        self._value = 5
        self._has_moved = False

    @property
    def has_moved(self):
        return self._has_moved

    @has_moved.setter
    def has_moved(self, boolean):
        self._has_moved = boolean

    def legal_moves(self, board, square):
        def is_legal_move(square):
            return self._is_legal_move(board, square)

        potential_moves = get_board_row(board, square) | get_board_column(board, square)
        return set(filter(is_legal_move, potential_moves))

    @staticmethod
    def white_ascii_representation():
        return 'R'

    @staticmethod
    def black_ascii_representation():
        return 'r'

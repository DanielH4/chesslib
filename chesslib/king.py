from chesslib.piece import Piece
from chesslib.rook import Rook
from chesslib.chess_board_utils import (
        get_adjacent_pieces,
        get_surrounding_squares
)


class King(Piece):
    def __init__(self, color):
        self._color = color
        self._value = None
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

        return set(filter(is_legal_move, get_surrounding_squares(square))) | self._legal_castling_moves(board, square)

    def _legal_castling_moves(self, board, square):
        if self.has_moved:
            return set()

        moves = set()
        for adjacent_piece in get_adjacent_pieces(board, square):
            if (
                isinstance(adjacent_piece, Rook) and
                self.has_moved == False and
                adjacent_piece.has_moved == False and
                adjacent_piece.color == self.color
            ):
                moves.add(board.get_square(adjacent_piece))
        return moves

    @staticmethod
    def white_ascii_representation():
        return 'K'

    @staticmethod
    def black_ascii_representation():
        return 'k'

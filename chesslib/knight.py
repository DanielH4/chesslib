from chesslib.piece import Piece
from chesslib.chess_board_utils import square_to_index, index_to_square, is_in_board


class Knight(Piece):
    def __init__(self, color):
        self._type = 'knight'
        self._color = color
        self._value = 3

    def legal_moves(self, board, square):
        def is_legal_move(square):
            return self._is_legal_move(board, square)

        square_index = square_to_index(square)

        potential_moves = set()
        for row_change in (-2,-1,1,2):
            for col_change in (-2,-1,1,2):
                if abs(row_change) != abs(col_change) and is_in_board(square_index, row_change, col_change):
                    potential_move = index_to_square(square_index + col_change + (8 * row_change))
                    potential_moves.add(potential_move)

        return set(filter(is_legal_move, potential_moves))

    @staticmethod
    def white_ascii_representation():
        return 'N'

    @staticmethod
    def black_ascii_representation():
        return 'n'

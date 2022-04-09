from chesslib.piece import Piece
from chesslib.chess_board_utils import get_board_diagonals


class Bishop(Piece):
    def __init__(self, color):
        self._color = color
        self._value = 3

    def legal_moves(self, board, square):
        def is_legal_move(square):
            piece = board.get_piece(square)

            # legal move if square is empty or pieces have different colors
            if piece == None or piece.color != self.color:
                return True
            return False

        return set(filter(is_legal_move, get_board_diagonals(board, square)))

    @staticmethod
    def white_ascii_representation():
        return 'B'

    @staticmethod
    def black_ascii_representation():
        return 'b'

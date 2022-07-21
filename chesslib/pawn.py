from chesslib.piece import Piece
from chesslib.chess_board_utils import (
    index_to_square,
    square_to_index, 
    get_n_front_squares,
    get_front_diagonal_squares,
    get_adjacent_pieces
)


class Pawn(Piece):
    def __init__(self, color):
        self._color = color
        self._value = 1
        self._en_passantable = False

    @property
    def en_passantable(self):
        return self._en_passantable

    @en_passantable.setter
    def en_passantable(self, boolean):
        self._en_passantable = boolean

    def legal_moves(self, board, square):
        return self._legal_row_moves(board, square) | self._legal_diagonal_moves(board, square)

    def _legal_row_moves(self, board, square):
        moves = set()

        n_front_squares = 2 if self.__class__._is_in_default_position(self, square) else 1

        for front_square in get_n_front_squares(board, square, self.color, n_front_squares):
            if board.is_empty_square(front_square):
                moves.add(front_square)

        return moves

    def _legal_diagonal_moves(self, board, square):
        moves = set()

        for diagonal_square in get_front_diagonal_squares(square, self.color):
            piece = board.get_piece(diagonal_square)

            if not board.is_empty_square(diagonal_square) and piece.color != self.color:
                moves.add(diagonal_square)

        for adjacent_piece in get_adjacent_pieces(board, square, col_limit=1):
            if isinstance(adjacent_piece, Pawn) and adjacent_piece.en_passantable:
                adjacent_piece_index = square_to_index(board.get_square(adjacent_piece))
                offset = 8 if self.color == 'white' else -8
                diagonal_square = index_to_square(adjacent_piece_index + offset)
                moves.add(diagonal_square)

        return moves

    @staticmethod
    def _is_in_default_position(pawn, square):
        square_index = square_to_index(square)
        row = int(square_index / 8) + 1

        is_white_default = (row == 2 and pawn.color == 'white')
        is_black_default = (row == 7 and pawn.color == 'black')
        
        if is_white_default or is_black_default:
            return True

        return False

    @staticmethod
    def white_ascii_representation():
        return 'P'

    @staticmethod
    def black_ascii_representation():
        return 'p'

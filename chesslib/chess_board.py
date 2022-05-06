from chesslib.king import King
from chesslib.pawn import Pawn
from chesslib.rook import Rook
from chesslib.queen import Queen
from chesslib.bishop import Bishop
from chesslib.knight import Knight
from chesslib.chess_board_utils import *


EMPTY_SQUARE_ASCII_REPRESENTATION = '.'


class InvalidBoardSizeError(ValueError):
    def __init__(self, num_squares, message=None):
        self._num_squares = num_squares
        if message is None:
            self._message = f"{num_squares} squares is not a valid board size." \
                             " A classic chess board has 64 squares."

    def __str__(self):
        return self._message


def create_default_board():
    board = [None] * 64

    for square_index in range(8,16):
        board[square_index] = Pawn('white')

    for square_index in range(48,56):
        board[square_index] = Pawn('black')

    board[square_to_index('a1')] = Rook('white')
    board[square_to_index('b1')] = Knight('white')
    board[square_to_index('c1')] = Bishop('white')
    board[square_to_index('d1')] = Queen('white')
    board[square_to_index('e1')] = King('white')
    board[square_to_index('f1')] = Bishop('white')
    board[square_to_index('g1')] = Knight('white')
    board[square_to_index('h1')] = Rook('white')

    board[square_to_index('a8')] = Rook('black')
    board[square_to_index('b8')] = Knight('black')
    board[square_to_index('c8')] = Bishop('black')
    board[square_to_index('d8')] = Queen('black')
    board[square_to_index('e8')] = King('black')
    board[square_to_index('f8')] = Bishop('black')
    board[square_to_index('g8')] = Knight('black')
    board[square_to_index('h8')] = Rook('black')

    return board


def create_board_from_str(board_str):
    if len(board_str) != 64:
        raise InvalidBoardSizeError(len(board_str))

    board = [None] * 64

    for square_index, char in enumerate(board_str):
        if char == EMPTY_SQUARE_ASCII_REPRESENTATION:
            pass
        elif char == Bishop.white_ascii_representation():
            board[square_index] = Bishop('white')
        elif char == Bishop.black_ascii_representation():
            board[square_index] = Bishop('black')
        elif char == Rook.white_ascii_representation():
            board[square_index] = Rook('white')
        elif char == Rook.black_ascii_representation():
            board[square_index] = Rook('black')
        elif char == Knight.white_ascii_representation():
            board[square_index] = Knight('white')
        elif char == Knight.black_ascii_representation():
            board[square_index] = Knight('black')
        elif char == King.white_ascii_representation():
            board[square_index] = King('white')
        elif char == King.black_ascii_representation():
            board[square_index] = King('black')
        elif char == Queen.white_ascii_representation():
            board[square_index] = Queen('white')
        elif char == Queen.black_ascii_representation():
            board[square_index] = Queen('black')
        elif char == Pawn.white_ascii_representation():
            board[square_index] = Pawn('white')
        elif char == Pawn.black_ascii_representation():
            board[square_index] = Pawn('black')
        else:
            raise UnicodeDecodeError('ChessBoard constructor',
                                     str.encode(board_str),
                                     square_index,
                                     square_index+1,
                                     f"Character '{char}' does not represent a" \
                                      " piece or empty square on the chess board.")

    return board


class ChessBoard():
    def __init__(self, board_str=None, empty=False):
        if empty:
            self._board = [None] * 64
        elif board_str is not None:
            self._board = create_board_from_str(board_str)
        else:
            self._board = create_default_board()

    def get_piece(self, square):
        return self._board[square_to_index(square)]

    # returns a list of all the pieces on the board or only pieces of specified color
    def get_pieces(self, color=None):
        if color is None:
            return [piece for piece in self._board if piece is not None]
        return [piece for piece in self._board if piece is not None and piece.color == color]

    def set_square(self, square, piece):
        self._board[square_to_index(square)] = piece

    def is_empty_square(self, square):
        return self.get_piece(square) is None

    def __str__(self):
        board_str = ''

        for square_index, piece in enumerate(self._board):
            if square_index % 8 == 0 and square_index > 0:
                board_str += '\n'

            if piece is None:
                board_str += '.'
            elif piece.color == 'white':
                board_str += piece.white_ascii_representation()
            else:
                board_str += piece.black_ascii_representation()

        return board_str

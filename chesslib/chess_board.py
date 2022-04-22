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
    return [None] * 64


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
    def __init__(self, board_str=None):
        if board_str == None:
            self._board = create_default_board()
        else:
            self._board = create_board_from_str(board_str)

    def get_piece(self, square):
        return self._board[square_to_index(square)]

    def is_empty_square(self, square):
        return self.get_piece(square) is None

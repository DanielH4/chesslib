from copy import deepcopy

from chesslib.pawn import Pawn
from chesslib.rook import Rook
from chesslib.queen import Queen
from chesslib.bishop import Bishop
from chesslib.knight import Knight
from chesslib.chess_board import ChessBoard
from chesslib.chess_board_utils import (
    index_to_square,
    square_to_index
)


class Chess():
    def __init__(self):
        self._board = ChessBoard()
        self._turn = 'white'
        self._check = False
        self._checkmate = False

    @property
    def turn(self):
        return self._turn

    @property
    def check(self):
        return self._check

    @property
    def checkmate(self):
        return self._checkmate

    # returns a set of tuples of the legal moves of a color
    # moves are encoded as squares (eg. 'c4') in the form: (from, to)
    def legal_moves(self, color=None):
        if color is None:
            color = self.turn

        def is_legal_move(move):
            game_copy = deepcopy(self)
            game_copy._board.move(move[0], move[1])
            if game_copy._is_check(color):
                return False
            return True

        return set(filter(is_legal_move, self._board.get_moves(color)))

    # moves a piece if it's a legal move otherwise returns None
    # if a legal move is made, returns value of the captured piece or 0 if captured square is empty
    def move(self, from_square, to_square, promote_to='queen'):
        if (not (from_square, to_square) in self.legal_moves(self.turn)) or self.checkmate:
            return None

        captured_piece = self._board.get_piece(to_square)

        self._handle_en_passant(from_square, to_square)
        self._board.move(from_square, to_square)

        if self._should_promote(to_square):
            self._promote(to_square, promote_to)

        self._swap_turn()

        self._check = True if self._is_check() else False
        self._checkmate = True if self._is_checkmate() else False

        if captured_piece is not None:
            return captured_piece.value
        return 0

    def print(self):
        status = ''
        if self.checkmate:
            status += 'Checkmate: '
            if self.turn == 'white':
                status += 'black wins!'
            else:
                status += 'white wins!'
        else:
            status += (f"Turn: {self.turn}\n"
                       f"Check: {self.check}")

        board_str = ''
        for square_index, char in enumerate(self._board.to_string(self.turn)):
            if square_index % 8 == 0 and square_index != 0:
                board_str += '\n'
            board_str += char

        print(status)
        print(board_str)

    def _handle_en_passant(self, from_square, to_square):
        moved_piece = self._board.get_piece(from_square)
        target_piece = self._board.get_piece(to_square)
        from_square_index = square_to_index(from_square)
        to_square_index = square_to_index(to_square)
        index_diff = abs(from_square_index - to_square_index)

        is_diagonal_move = (index_diff == 7) or (index_diff == 9)
        is_double_move = (index_diff == 16)

        # remove adjacent pawn if it's a passant move
        if isinstance(moved_piece, Pawn) and is_diagonal_move and target_piece is None:
            square_offset = -8 if self.turn == 'white' else 8
            adjacent_square = index_to_square(to_square_index + square_offset)
            self._board.set_square(adjacent_square, None)

        # clear passant flags
        for piece in self._board.get_pieces(self.turn):
            if isinstance(piece, Pawn):
                piece.en_passantable = False

        # set passant flag
        if isinstance(moved_piece, Pawn) and is_double_move and Pawn._is_in_default_position(moved_piece, from_square):
            moved_piece.en_passantable = True

    def _should_promote(self, square):
        row = int(square[1])
        piece = self._board.get_piece(square)
        is_last_rank = ((piece.color == 'white' and row == 8)
                        or
                        (piece.color == 'black' and row == 1))

        if isinstance(piece, Pawn) and is_last_rank:
            return True
        return False

    def _promote(self, square, promote_to):
        piece = None
        if promote_to == 'rook':
            piece = Rook(self.turn)
        elif promote_to == 'bishop':
            piece = Bishop(self.turn)
        elif promote_to == 'knight':
            piece = Knight(self.turn)
        else:
            piece = Queen(self.turn)

        self._board.set_square(square, piece)

    def _is_check(self, color=None):
        if color is None:
            color = self.turn

        king_square = self._board.get_king_square(color)
        opponent_color = 'white' if color == 'black' else 'black'

        for (_, to_square) in self._board.get_moves(opponent_color):
            if to_square == king_square:
                return True
        return False

    def _is_checkmate(self, color=None):
        if color is None:
            color = self.turn

        if self.legal_moves(color) == set():
            return True
        return False

    def _swap_turn(self):
        if self.turn == 'white':
            self._turn = 'black'
        else:
            self._turn = 'white'

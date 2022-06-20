from copy import deepcopy

from chesslib.chess_board import ChessBoard


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
    def move(self, from_square, to_square):
        if (not (from_square, to_square) in self.legal_moves(self.turn)) or self.checkmate:
            return None

        captured_piece = self._board.get_piece(to_square)

        self._board.move(from_square, to_square)
        self._swap_turn()

        self._check = True if self._is_check() else False
        self._checkmate = True if self._is_checkmate() else False

        if captured_piece is not None:
            return captured_piece.value
        return 0

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

from chesslib.chess_board import ChessBoard


class Chess():
    def __init__(self):
        self._board = ChessBoard()
        self._turn = 'white'

    @property
    def turn(self):
        return self._turn

    # returns a set of tuples of the legal moves of a color
    # moves are encoded as squares (eg. 'c4') in the form: (from, to)
    def legal_moves(self, color=None):
        if color is None:
            color = self.turn

        moves = set()
        for piece in self._board.get_pieces(color):
            from_square = self._board.get_square(piece)
            for to_square in piece.legal_moves(self._board, from_square):
                moves.add((from_square, to_square))
        return moves

    def _swap_turn(self):
        if self.turn == 'white':
            self._turn = 'black'
        else:
            self._turn = 'white'

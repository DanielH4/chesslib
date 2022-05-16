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

        moves = set()
        for piece in self._board.get_pieces(color):
            from_square = self._board.get_square(piece)
            for to_square in piece.legal_moves(self._board, from_square):
                moves.add((from_square, to_square))
        return moves

    # moves a piece if it's a legal move otherwise returns None
    # if a legal move is made, returns value of the captured piece or 0 if captured square is empty
    def move(self, from_square, to_square):
        if not (from_square, to_square) in self.legal_moves(self.turn):
            return None

        moved_piece = self._board.get_piece(from_square)
        captured_piece = self._board.get_piece(to_square)

        self._board.set_square(to_square, moved_piece)
        self._board.set_square(from_square, None)
        self._swap_turn()

        if captured_piece is not None:
            return captured_piece.value
        return 0

    def _swap_turn(self):
        if self.turn == 'white':
            self._turn = 'black'
        else:
            self._turn = 'white'

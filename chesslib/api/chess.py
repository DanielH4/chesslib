from chesslib.chess_board import ChessBoard


class Chess():
    def __init__(self):
        self._board = ChessBoard()
        self._turn = 'white'

    @property
    def turn(self):
        return self._turn

    def _swap_turn(self):
        if self.turn == 'white':
            self._turn = 'black'
        else:
            self._turn = 'white'

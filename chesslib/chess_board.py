from chesslib.bishop import Bishop


def create_default_board():
    return [None] * 64


class ChessBoard():
    def __init__(self):
        self._board = create_default_board()

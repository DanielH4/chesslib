def create_default_board():
    return [None] * 64


class ChessBoard():
    def __init__(self):
        self._board = create_default_board()

    def get_piece(self, square):
        return self._board[square_to_index(square)]

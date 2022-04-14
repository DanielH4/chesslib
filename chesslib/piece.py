from abc import ABC, abstractmethod


class Piece(ABC):
    @property
    def color(self):
        return self._color

    @property
    def value(self):
        return self._value

    @staticmethod
    @abstractmethod
    def white_ascii_representation():
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def black_ascii_representation():
        raise NotImplementedError

    @abstractmethod
    def legal_moves(self, board, square):
        raise NotImplementedError

    # returns true if given square is unoccupied on the board 
    # or if occupying piece has a different color
    def _is_legal_move(self, board, square):
        piece = board.get_piece(square)

        if board.is_empty_square(square) or piece.color != self.color:
            return True
        return False
    
    def __str__(self):
        if self.color == 'white':
            return self.__class__.white_ascii_representation()
        return self.__class__.black_ascii_representation()

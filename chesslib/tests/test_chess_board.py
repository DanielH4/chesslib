import pytest

from chesslib.chess_board import *


def test_create_board_from_str():
    with pytest.raises(InvalidBoardSizeError) as e_info:
        create_board_from_str("...")
    with pytest.raises(UnicodeDecodeError) as e_info:
        create_board_from_str("x......."
                              "........"
                              "........"
                              "........"
                              "........"
                              "........"
                              "........"
                              "........")

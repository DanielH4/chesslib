import os
import json
import pytest
import jsonschema

from chesslib.api import Chess
from chesslib.king import King
from chesslib.rook import Rook
from chesslib.queen import Queen
from chesslib.chess_board import ChessBoard


@pytest.fixture
def get_json_str_from_testdata():
    def get_testdata_file_path(file_name):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return f'{dir_path}/testdata/{file_name}'

    def get_json_str(file_name):
        with open(get_testdata_file_path(file_name), 'r') as f:
            data = json.load(f)
            return json.dumps(data)

    return get_json_str


def test_legal_moves():
    game = Chess()
    game._board = ChessBoard("........"
                             "........"
                             "........"
                             "........"
                             "........"
                             "........"
                             "........"
                             "Rn......")
    white_rook_legal_moves = {
        ('a8', 'a7'),
        ('a8', 'a6'),
        ('a8', 'a5'),
        ('a8', 'a4'),
        ('a8', 'a3'),
        ('a8', 'a2'),
        ('a8', 'a1'),
        ('a8', 'b8')
    }
    black_knight_legal_moves = {
        ('b8', 'a6'),
        ('b8', 'c6'),
        ('b8', 'd7')
    }

    assert (
        (game.legal_moves('white') == white_rook_legal_moves)
        and
        (game.legal_moves('black') == black_knight_legal_moves)
    )


def test_legal_moves():
    game = Chess()
    game._board = ChessBoard(".K......"
                             "q......."
                             "pp......"
                             "........"
                             "........"
                             "........"
                             "........"
                             "........")
    king_square = 'b1'
    queen_square = 'a2'
    pawn_square = 'b3'
    assert (
        game.legal_moves('white') == {(king_square, 'c1')}
        and
        game.legal_moves('black') == {
                                        (queen_square, 'a1'),
                                        (queen_square, 'b1'),
                                        (queen_square, 'b2'),
                                        (queen_square, 'c2'),
                                        (queen_square, 'd2'),
                                        (queen_square, 'e2'),
                                        (queen_square, 'f2'),
                                        (queen_square, 'g2'),
                                        (queen_square, 'h2'),
                                        (pawn_square, 'b2')
                                     }
    )

def test_move():
    game1 = Chess()
    game1._turn = 'white'
    game1._board = ChessBoard("......k."
                              "....Q..."
                              "........"
                              "........"
                              "........"
                              "........"
                              "........"
                              "........")
    game1.move('e2', 'f2')

    game2 = Chess()
    game2._turn = 'black'
    game2._board = ChessBoard("......k."
                              ".....Q.."
                              "........"
                              "........"
                              "........"
                              "........"
                              "........"
                              "........")
    game2.move('g1', 'h1')

    game3 = Chess()
    game3._turn = 'white'
    game3._board = ChessBoard(".......k"
                              ".....Q.."
                              "........"
                              "........"
                              "........"
                              "........"
                              "........"
                              "......R.")
    game3.move('f2', 'g2')

    game4 = Chess()
    game4._turn = 'black'
    game4._board = ChessBoard("..K....."
                              "p......."
                              "........"
                              "....k..."
                              "........"
                              "........"
                              "........"
                              "........")
    game4.move('a2', 'a1')
    game4_promoted_piece = game4._board.get_piece('a1')

    game5 = Chess()
    game5._turn = 'white'
    game5._board = ChessBoard("........"
                              "P......."
                              "........"
                              ".p......"
                              "........"
                              "........"
                              "........"
                              "........")
    game5.move('a2', 'a4')
    game5_en_passantable = game5._board.get_piece('a4').en_passantable
    game5.move('b4', 'a3')
    game5_en_passantable_capture = game5._board.get_piece('a4') is None

    game6 = Chess()
    game6._turn = 'black'
    game6._board = ChessBoard("........"
                              "........"
                              "........"
                              "........"
                              "...P...."
                              "........"
                              "....p..."
                              "........")
    game6.move('e7', 'e5')
    game6_en_passantable = game6._board.get_piece('e5').en_passantable
    game6.move('d5', 'e6')
    game6_en_passantable_capture = game6._board.get_piece('e5') is None

    game7 = Chess()
    game7._turn = 'white'
    game7._board = ChessBoard("R...K..."
                              "........"
                              "........"
                              "........"
                              "........"
                              "........"
                              "........"
                              "....k..r")
    game7.move('e1', 'a1')
    game7.move('e8', 'h8')
    expected_game7_white_king_square = 'c1'
    expected_game7_white_rook_square = 'd1'
    expected_game7_black_king_square = 'g8'
    expected_game7_black_rook_square = 'f8'

    assert (
        game1.turn == 'black'
        and
        game1.in_check == True
        and
        game1.checkmate == False
        and
        game2.in_check == False
        and
        game3.checkmate == True
        and
        isinstance(game4_promoted_piece, Queen)
        and
        game4.in_check == True
        and
        game5_en_passantable == True
        and
        game5_en_passantable_capture == True
        and
        game6_en_passantable == True
        and
        game6_en_passantable_capture == True
        and
        isinstance(game7._board.get_piece(expected_game7_white_king_square), King)
        and
        isinstance(game7._board.get_piece(expected_game7_white_rook_square), Rook)
        and
        isinstance(game7._board.get_piece(expected_game7_black_king_square), King)
        and
        isinstance(game7._board.get_piece(expected_game7_black_rook_square), Rook)
    )


def test_from_json_default_chess(get_json_str_from_testdata):
    chess_json_str = get_json_str_from_testdata('default_chess.json')
    from_json = Chess.fromJSON(chess_json_str)

    assert from_json == Chess()


def test_from_json_missing_properties_rook(get_json_str_from_testdata):
    chess_json_str = get_json_str_from_testdata('chess_missing_properties_rook.json')
    with pytest.raises(jsonschema.exceptions.ValidationError):
        Chess.fromJSON(chess_json_str)

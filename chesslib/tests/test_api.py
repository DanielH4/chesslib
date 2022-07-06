from chesslib.api import Chess
from chesslib.queen import Queen
from chesslib.chess_board import ChessBoard


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

    assert (
        game1.turn == 'black'
        and
        game1.check == True
        and
        game1.checkmate == False
        and
        game2.check == False
        and
        game3.checkmate == True
        and
        isinstance(game4_promoted_piece, Queen)
        and
        game4.check == True
    )

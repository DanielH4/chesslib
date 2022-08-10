from chesslib.api import Chess


if __name__ == '__main__':
    game = Chess()
    game.print()
    while not game.checkmate:
        while True:
            from_square = input("Move from:")
            to_square = input("Move to:")
            if game.move(from_square, to_square) is not None:
                break
            else:
                print('Invalid move.')
        print()
        game.print()
    print("Game Over!")

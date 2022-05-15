"""
Game engine
"""
import sys

from board import Board

def main():
    print("Game of Tic-Tac-Toe")
    board = Board()

    def get_input(message):
        while True:
            output = input(message)
            try:
                output = int(output)
                if not 0 <= output <= 2:
                    print("Wrong coordinate. Try again. "
                          "Coordinate must be from 0 to 2")
                else:
                    return output
            except (TypeError, ValueError):
                print("Wrong input. Try again. "
                      "Coordinate must be integer from 0 to 2")


    while True:
        print(board)
        x = get_input("Enter the X coordinate: ")
        y = get_input("Enter the Y coordinate: ")
        try:
            board.make_move((y,x), "X")
        except KeyError:
            print("That cell is occupied. Try other one")
            continue
        if board.get_status() == "continue":
            pass
        elif board.get_status() == "draw":
            print("It's a DRAW")
            sys.exit()
        else:
            print(f"{board.get_status()} wins")
            sys.exit()
        board.make_computer_move()



if __name__ == "__main__":
    main()
    board = Board()
    print(board)
    board.make_move((1,1), "X")
    # board.make_move((1, 2), "X")
    board.make_move((1, 0), "X")
    # board.make_move((0, 0), "X")
    board.make_move((2, 2), "X")
    # board.make_move((0, 2), "X")
    board.make_move((2, 0), "O")
    board.make_move((2, 1), "X")

    print(board)
    print(board.get_status())
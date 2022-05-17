"""
Game engine
"""
import sys

from board import Board

def main():
    """
    Main function of game, that runs all scripts
    @return:
    """
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

    def check_end(board):
        """
        Function to check if the game ended
        @param board:
        @return:
        """
        if board.get_status() == "continue":
            pass
        elif board.get_status() == "draw":
            print(board)
            print("It's a DRAW")
            sys.exit()
        else:
            print(board)
            print(f"{board.get_status()} wins")
            sys.exit()

    while True:
        print(board)
        x = get_input("Enter the X coordinate: ")
        y = get_input("Enter the Y coordinate: ")
        try:
            board.make_move((y,x), "x")
        except KeyError:
            print("That cell is occupied. Try other one")
            continue
        check_end(board)
        board.make_computer_move()
        check_end(board)



if __name__ == "__main__":
    # main()
    board = Board()
    board.make_move((0, 0), "x")
    board.make_move((0, 1), "x")
    board.make_move((1, 0), "0")
    board.make_move((0, 2), "0")
    print(board, end="\n\n")
    board.make_computer_move()
    print(board, end="\n\n")
    board.make_move((2, 2), "x")
    board.make_computer_move()
    print(board, end="\n\n")
    print(board.get_status())
    try:
        board.make_move((4, 4), "")
    except IndexError as err:
        print(err)
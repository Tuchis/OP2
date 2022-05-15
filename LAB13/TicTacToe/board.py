"""
Board class
"""
from btree import LinkedBinaryTree
import copy

class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.last_turn = None

    def __str__(self):
        output = ""
        for row in range(len(self.board)):
            output += str(self.board[row]) + "\n"
        return output[:-1]


    def get_status(self):
        """
        Method to check if the game ended (4 possible outputs: 'X', 'O', 'draw',
        'continue')
        @return:
        """
        # Horizontal check
        for row in range(3):
            sign = None
            count = 0
            for col in range(3):
                if (sign is None and self.board[row][col] == "X") or \
                        (sign is None and self.board[row][col] == "O")\
                        or sign == self.board[row][col]:
                    sign = self.board[row][col]
                    count += 1
                else:
                    continue
            if count == 3:
                return sign

        # Vertical check
        for col in range(3):
            sign = None
            count = 0
            for row in range(3):
                if (sign is None and self.board[row][col] == "X") or \
                        (sign is None and self.board[row][col] == "O")\
                        or sign == self.board[row][col]:
                    sign = self.board[row][col]
                    count += 1
                else:
                    continue
            if count == 3:
                return sign

        # Diagonal check
        for set_of_coord in [[(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]]:
            sign = None
            count = 0
            for row, col in set_of_coord:
                if (sign is None and self.board[row][col] == "X") or \
                        (sign is None and self.board[row][col] == "O")\
                        or sign == self.board[row][col]:
                    sign = self.board[row][col]
                    count += 1
                else:
                    continue
            if count == 3:
                return sign

        # Draw check
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    return "continue"
        return "draw"

    def make_move(self, position, turn):
        """
        Method for players moves
        @param position:
        @param turn:
        @return:
        """
        if not isinstance(position[0], int) or not isinstance(position[1], int)\
        or position[0] > 2 or position[0] < 0 \
        or position[1] > 2 or position[1] < 0:
            raise IndexError
        if self.board[position[0]][position[1]] == " ":
            self.board[position[0]][position[1]] = turn
            self.last_turn = (position[0], position[1])
            print(self.last_turn)
        else:
            raise KeyError
        return self

    @staticmethod
    def get_two_moves(board):
        lister = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == " " and len(lister) != 2:
                    lister.append((row, col))
        return lister


    def make_computer_move(self):
        decision_tree = LinkedBinaryTree(self)
        def recurse_create(root):
            moves = Board.get_two_moves(root.key.board)
            if len(moves) == 1:
                decision_tree.insert_left(recurse_create(copy.deepcopy(root.key).make_move(moves[0], "O")))
            else:
                print(copy.deepcopy(root.key))
                # print(root.key.make_move(moves[0], "O"))
                print(copy.deepcopy(root.key).make_move(moves[0], "O"))
                decision_tree.insert_left(recurse_create(copy.deepcopy(root.key).make_move(moves[0], "O")))
                decision_tree.insert_right(recurse_create(copy.deepcopy(root.key).make_move(moves[1], "O")))

        def recurse_sum(root):
            if root.key is None:
                return 0
            if root.key.get_status() == "draw":
                return 0
            elif root.key.get_status() == "O":
                return 1
            elif root.key.get_status() == "X":
                return -1
            else:
                return recurse_sum(root.get_left_child()) + recurse_sum(root.get_right_child())


        recurse_create(decision_tree)
        print(recurse_sum(decision_tree))

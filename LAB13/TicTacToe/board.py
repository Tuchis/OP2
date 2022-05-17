"""
Board class
"""
from btree import LinkedBinaryTree
from btnode import Node
import copy


class Board:
    """
    Board class that contains board and processes every mechanic of the game
    """

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
        Method to check if the game ended (4 possible outputs: 'x', '0', 'draw',
        'continue')
        @return:
        """
        # Horizontal check
        for row in range(3):
            sign = None
            count = 0
            for col in range(3):
                if (sign is None and self.board[row][col] == "x") or \
                        (sign is None and self.board[row][col] == "0") \
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
                if (sign is None and self.board[row][col] == "x") or \
                        (sign is None and self.board[row][col] == "0") \
                        or sign == self.board[row][col]:
                    sign = self.board[row][col]
                    count += 1
                else:
                    continue
            if count == 3:
                return sign

        # Diagonal check
        for set_of_coord in [[(0, 0), (1, 1), (2, 2)],
                             [(0, 2), (1, 1), (2, 0)]]:
            sign = None
            count = 0
            for row, col in set_of_coord:
                if (sign is None and self.board[row][col] == "x") or \
                        (sign is None and self.board[row][col] == "0") \
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
        if not isinstance(position[0], int) or not isinstance(position[1], int) \
                or position[0] > 2 or position[0] < 0 \
                or position[1] > 2 or position[1] < 0:
            raise IndexError
        if self.board[position[0]][position[1]] == " ":
            self.board[position[0]][position[1]] = turn
            self.last_turn = (position[0], position[1])
        else:
            raise IndexError
        return self

    @staticmethod
    def get_two_moves(board):
        """
        Function that returns two moves, that are sorted by the Y coordinate,
        then by X coordinate
        @param board:
        @return:
        """
        lister = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == " " and len(lister) != 2:
                    lister.append((row, col))
        return lister

    def make_computer_move(self):
        """
        Function that makes move of computer
        @return:
        """
        decision_tree = LinkedBinaryTree(self)

        def recurse_create(root, turn="0"):
            if root.value.get_status() != "continue":
                returns = {"0": 1,
                           "x": -1,
                           "draw": 0}
                return returns[root.value.get_status()]
            moves = Board.get_two_moves(root.value.board)
            if len(moves) == 0:
                return "draw"
            elif len(moves) == 1:
                root.insert_left(recurse_create(Node(
                    copy.deepcopy(root.value).make_move(moves[0], turn)),
                    "0" if turn == "x" else "x"))
            else:
                root.insert_left(recurse_create(Node(
                    copy.deepcopy(root.value).make_move(moves[0], turn)),
                    "0" if turn == "x" else "x"))
                root.insert_right(recurse_create(Node(
                    copy.deepcopy(root.value).make_move(moves[1], turn)),
                    "0" if turn == "x" else "x"))
            return root

        def recurse_sum(root):
            """
            Fuction that sums the leaves of bin tree
            @param root:
            @return:
            """
            if root is None:
                return 0
            if isinstance(root, int):
                return root
            else:
                return recurse_sum(root.get_left_child()) + \
                       recurse_sum(root.get_right_child())

        recurse_create(decision_tree.key)
        if isinstance(decision_tree.key.left_child,
                      int) and decision_tree.key.left_child == 1:
            self.make_move(Board.get_two_moves(self.board)[0], "0")
        elif isinstance(decision_tree.key.left_child,
                      int) and decision_tree.key.right_child == 1:
            self.make_move(Board.get_two_moves(self.board)[1], "0")
        else:
            self.make_move(Board.get_two_moves(self.board)[0]
                       if recurse_sum(decision_tree.key.left_child) >
                          recurse_sum(decision_tree.key.right_child)
                       else self.get_two_moves(self.board)[1], "0")

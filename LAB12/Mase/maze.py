"""Implemention of the Maze ADT using a 2-D array."""
import time

from arrays import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, num_rows, num_cols):
        """Creates a maze object with all cells marked as open."""
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)


    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        path = Stack()
        path.push(self._start_cell)
        cell = path.peek()
        while not path.is_empty():
            if self._valid_move(cell.row, cell.col):
                self._mark_path(cell.row, cell.col)
                # path.push(_CellPosition(cell.row, cell.col))
            if self._exit_found(cell.row, cell.col):
                return True
            dead_end = True
            for row, col in [(-1,0), (0,1), (1,0), (0,-1)]:
                if self._valid_move(cell.row + row, cell.col + col):
                    dead_end = False
                    # self._mark_path(cell.row + row, cell.col + col)
                    path.push(_CellPosition(cell.row + row, cell.col + col))
                    cell = path.peek()
                    break
            if dead_end:
                self._mark_tried(cell.row, cell.col)
                path.pop()
                try:
                    cell = path.peek()
                except AssertionError:
                    return False
        return False

    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self._maze_cells[row, col] in [self.TRIED_TOKEN, self.PATH_TOKEN]:
                    self._maze_cells[row, col] = None

    def __str__(self):
        """Returns a text-based representation of the maze."""
        output = ""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                output += str(self._maze_cells[row, col]) + " " \
                    if self._maze_cells[row, col] != None else "_ "
                if col == self.num_cols() - 1 and row != self.num_rows() - 1:
                    output += "\n"
        return output

    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return 0 <= row < self.num_rows() \
               and 0 <= col < self.num_cols() \
               and self._maze_cells[row, col] is None

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition(object):
    """Private storage class for holding a cell position."""
    def __init__(self, row, col):
        self.row = row
        self.col = col


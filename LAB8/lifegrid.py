from arrays import Array2D


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.
        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.
        :return:Returns the number of columns in the grid.
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.

        :param coord_list:
        :return:
        """
        for elem in coord_list:
            self.set_cell(elem)

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?

        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        return True if self._grid.__getitem__((row,col)) == self.LIVE_CELL \
            else False

    def clear_cell(self, coord):
        """
        Clears the indicated cell by setting it to dead.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid.__setitem__(coord, self.DEAD_CELL)

    def set_cell(self, coord):
        """
        Sets the indicated cell to be alive.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid.__setitem__(coord, self.LIVE_CELL)

    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.
        :param row: row of the cell.
        :param col: column of the cell.
        :return:
        """
        count = 0
        for x in range(3):
            for y in range(3):
                try:
                    count += 1 if self._grid.__getitem__((row + y - 1, col + x -1)) == self.LIVE_CELL else 0
                except AssertionError:
                    pass
        if self._grid.__getitem__((row, col)) == self.LIVE_CELL:
            count -= 1
        return count

    def __str__(self):
        """
        Returns string representation of LifeGrid
        in form of:
        DDLDD
        DLDLD
        DLDLD
        DDLDD
        DDDDD
        Where D - dead cell, L - live cell
        """
        s = ""
        for row in range(self._grid.num_rows()):
            for col in range(self._grid.num_cols()):
                s += "L" if self._grid.__getitem__((row, col)) == self.LIVE_CELL else "D"
                s += "\n" if row != (self._grid.num_rows() - 1) \
                    and col == (self._grid.num_cols() - 1) else ""
        return s

if __name__ == "__main__":
    a = LifeGrid(5,5)
    a.se
    print(a)
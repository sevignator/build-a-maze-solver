import random
import time

from cell import Cell
from window import Window


class Maze:

    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window | None = None,
        seed: int | None = None,
    ):
        self._cells: list[list[Cell]] = []
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win: Window | None = win
        self._seed = seed

        # Set seed for debugging purposes
        if self._seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        # Create columnss
        for _ in range(self._num_cols):
            col_cells = []

            # Create rows for each column
            for _ in range(self._num_rows):
                col_cells.append(Cell(self._win))

            self._cells.append(col_cells)

        # Draw cells
        for col_idx in range(self._num_cols):
            for row_idx in range(self._num_rows):
                self._draw_cell(col_idx, row_idx)

    def _draw_cell(self, i, j):
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()

        # Default delay: 0.05
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        # Break entrance
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        # Break exit
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i: int, j: int):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            available_indexes = []

            # Check if the left cell can be visited
            if i > 0 and not self._cells[i - 1][j].visited:
                available_indexes.append((i - 1, j))

            # Check if the right cell can be visited
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                available_indexes.append((i + 1, j))

            # Check if the top cell can be visited
            if j > 0 and not self._cells[i][j - 1].visited:
                available_indexes.append((i, j - 1))

            # Check if the bottom cell can be visited
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                available_indexes.append((i, j + 1))

            # Exit if there's nowhere to go
            if len(available_indexes) == 0:
                self._draw_cell(i, j)
                return

            # Pick a random available cell
            direction_index = random.randrange(len(available_indexes))
            next_index = available_indexes[direction_index]

            # Break the right wall
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            # Break the left wall
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            # Break the top wall
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # Break the bottom wall
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _solve_r(self, i: int, j: int):
        self._animate()

        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if (
            i < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False

    def solve(self):
        return self._solve_r(0, 0)

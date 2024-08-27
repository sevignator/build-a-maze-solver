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
    ):
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win: Window | None = win

        self._cells: list[list[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()

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

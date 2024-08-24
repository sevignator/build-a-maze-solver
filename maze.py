import time
from cell import Cell
from window import Window


class Maze:

    def __init__(
        self,
        win: Window,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
    ):
        self._win: Window = win
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._cells: list = []

        self._create_cells()

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
        self._win.redraw()
        time.sleep(0.05)

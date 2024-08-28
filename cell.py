from line import Line
from point import Point
from window import Window


class Cell:
    def __init__(
        self,
        win: Window | None = None,
    ):
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.visited: bool = False
        self._x1: int | None = None
        self._y1: int | None = None
        self._x2: int | None = None
        self._y2: int | None = None
        self._win: Window | None = win

    def get_coords(self):
        return (self._x1, self._y1, self._x2, self._y2)

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        if self._win is None:
            return

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        left_line = Line(Point(x1, y1), Point(x1, y2))
        right_line = Line(Point(x2, y1), Point(x2, y2))
        top_line = Line(Point(x1, y1), Point(x2, y1))
        bottom_line = Line(Point(x1, y2), Point(x2, y2))

        if self.has_left_wall:
            self._win.draw_line(left_line)
        else:
            self._win.draw_line(left_line, "white")

        if self.has_right_wall:
            self._win.draw_line(right_line)
        else:
            self._win.draw_line(right_line, "white")

        if self.has_top_wall:
            self._win.draw_line(top_line)
        else:
            self._win.draw_line(top_line, "white")

        if self.has_bottom_wall:
            self._win.draw_line(bottom_line)
        else:
            self._win.draw_line(bottom_line, "white")

    def draw_move(self, to_cell: "Cell", undo: bool = False):
        if self._win is None:
            return

        match undo:
            case True:
                color = "red"
            case _:
                color = "gray"

        (a_x1, a_y1, a_x2, a_y2) = self.get_coords()
        (b_x1, b_y1, b_x2, b_y2) = to_cell.get_coords()

        p1 = Point((a_x1 + a_x2) / 2, (a_y1 + a_y2) / 2)
        p2 = Point((b_x1 + b_x2) / 2, (b_y1 + b_y2) / 2)

        self._win.draw_line(Line(p1, p2), color)

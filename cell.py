from line import Line
from point import Point
from window import Window


class Cell:
    def __init__(
        self,
        win: Window,
        x1: int | None = None,
        y1: int | None = None,
        x2: int | None = None,
        y2: int | None = None,
        has_left_wall: bool = True,
        has_right_wall: bool = True,
        has_top_wall: bool = True,
        has_bottom_wall: bool = True,
    ):
        self._win: Window = win
        self._x1: int | None = x1
        self._y1: int | None = y1
        self._x2: int | None = x2
        self._y2: int | None = y2
        self.has_left_wall: bool = has_left_wall
        self.has_right_wall: bool = has_right_wall
        self.has_top_wall: bool = has_top_wall
        self.has_bottom_wall: bool = has_bottom_wall

    def get_coords(self):
        return (self._x1, self._y1, self._x2, self._y2)

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        lines = []

        if self.has_left_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            lines.append(Line(p1, p2))

        if self.has_right_wall:
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            lines.append(Line(p1, p2))

        if self.has_top_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            lines.append(Line(p1, p2))

        if self.has_bottom_wall:
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            lines.append(Line(p1, p2))

        for line in lines:
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell: "Cell", undo: bool = False):
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

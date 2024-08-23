from line import Line
from point import Point
from window import Window


class Cell:

    def __init__(
        self,
        win: Window,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ):
        self._x1: int = x1
        self._y1: int = y1
        self._x2: int = x2
        self._y2: int = y2
        self._win: Window = win
        self.has_left_wall: bool = has_left_wall
        self.has_right_wall: bool = has_right_wall
        self.has_top_wall: bool = has_top_wall
        self.has_bottom_wall: bool = has_bottom_wall

    def get_coords(self):
        return (self._x1, self._y1, self._x2, self._y2)

    def draw(self):
        lines = []

        if self.has_left_wall:
            point_a = Point(self._x1, self._y1)
            point_b = Point(self._x1, self._y2)
            lines.append(Line(point_a, point_b))

        if self.has_right_wall:
            point_a = Point(self._x2, self._y1)
            point_b = Point(self._x2, self._y2)
            lines.append(Line(point_a, point_b))

        if self.has_top_wall:
            point_a = Point(self._x1, self._y1)
            point_b = Point(self._x2, self._y1)
            lines.append(Line(point_a, point_b))

        if self.has_bottom_wall:
            point_a = Point(self._x1, self._y2)
            point_b = Point(self._x2, self._y2)
            lines.append(Line(point_a, point_b))

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

        point_a = Point((a_x1 + a_x2) / 2, (a_y1 + a_y2) / 2)
        point_b = Point((b_x1 + b_x2) / 2, (b_y1 + b_y2) / 2)

        self._win.draw_line(Line(point_a, point_b), color)

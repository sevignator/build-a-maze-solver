from tkinter import Canvas
from point import Point


class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self.point_a: Point = point_a
        self.point_b: Point = point_b

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.point_a.x,
            self.point_a.y,
            self.point_b.x,
            self.point_b.y,
            fill=fill_color,
            width=2,
        )

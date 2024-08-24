from tkinter import Canvas
from point import Point


class Line:
    def __init__(self, p1: Point, p2: Point):
        self._p1: Point = p1
        self._p2: Point = p2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self._p1.x,
            self._p1.y,
            self._p2.x,
            self._p2.y,
            fill=fill_color,
            width=2,
        )

from tkinter import Tk, BOTH, Canvas
from line import Line


class Window:
    def __init__(self, width: int, height: int):
        self._root = Tk()
        self._canvas = Canvas(self._root, bg="white", width=width, height=height)
        self._is_running = False

        # Stop the window from running when the user closes it
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._root.title("Maze Solver")
        self._canvas.pack()

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._is_running = True

        while self._is_running:
            self.redraw()

    def close(self):
        self._is_running = False

    def draw_line(self, line: Line, fill_color: str = "black"):
        line.draw(self._canvas, fill_color)

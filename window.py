from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__canvas = Canvas(width=width, height=height)
        self.__is_running = False

        # Stop the window from running when the user closes it
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title = "Maze Solver"
        self.__canvas.pack()

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True

        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

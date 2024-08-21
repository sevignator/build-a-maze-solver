from line import Line
from point import Point
from window import Window


def main():
    # Create the window object
    win = Window(800, 600)

    line_a = Line(Point(100, 100), Point(700, 500))
    line_b = Line(Point(100, 500), Point(700, 100))

    win.draw_line(line_a, "red")
    win.draw_line(line_b, "green")

    # Make the window object closable
    win.wait_for_close()


main()

from cell import Cell
from line import Line
from point import Point
from window import Window


def main():
    win = Window(800, 600)

    line_a = Line(Point(100, 100), Point(700, 500))
    line_b = Line(Point(100, 500), Point(700, 100))

    cell_a = Cell(win, 50, 50, 100, 100, has_left_wall=False)
    cell_b = Cell(win, 150, 150, 200, 200, has_top_wall=False)
    cell_c = Cell(win, 250, 50, 300, 100, has_right_wall=False)

    win.draw_line(line_a, "red")
    win.draw_line(line_b, "green")

    cell_a.draw()
    cell_b.draw()
    cell_c.draw()

    cell_a.draw_move(cell_b)
    cell_b.draw_move(cell_c, undo=True)

    win.wait_for_close()


main()

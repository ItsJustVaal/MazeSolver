from line import Line
from point import Point


class Cell:
    def __init__(self, window=None) -> None:
        self.left = True
        self.right = True
        self.top = True
        self.bottom = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.window = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.left:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw_line(line, "white")

        if self.top:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw_line(line, "white")

        if self.right:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw_line(line, "white")

        if self.bottom:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.window.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.window.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if self.window is None:
            return
        midOne = (self._x1 + self._x2) / 2
        midTwo = (self._y1 + self._y2) / 2

        toMidOne = (to_cell._x1 + to_cell._x2) / 2
        toMidTwo = (to_cell._y1 + to_cell._y2) / 2

        fill = "red"
        if undo:
            fill = "gray"

        # left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, midTwo), Point(midOne, midTwo))
            self.window.draw_line(line, fill)
            line = Line(Point(toMidOne, toMidTwo),
                        Point(to_cell._x2, toMidTwo))
            self.window.draw_line(line, fill)

        # right
        elif self._x1 < to_cell._x1:
            line = Line(Point(midOne, midTwo), Point(self._x2, midTwo))
            self.window.draw_line(line, fill)
            line = Line(Point(to_cell._x1, toMidTwo),
                        Point(toMidOne, toMidTwo))
            self.window.draw_line(line, fill)

        # up
        elif self._y1 > to_cell._y1:
            line = Line(Point(self._x1, midTwo), Point(midOne, self._y1))
            self.window.draw_line(line, fill)
            line = Line(Point(toMidOne, to_cell._y2),
                        Point(toMidOne, toMidTwo))
            self.window.draw_line(line, fill)

        # down
        elif self._y1 < to_cell._y1:
            line = Line(Point(midOne, midTwo), Point(midOne, self._y2))
            self.window.draw_line(line, fill)
            line = Line(Point(toMidOne, toMidTwo),
                        Point(toMidOne, to_cell._y1))
            self.window.draw_line(line, fill)

from tkinter import BOTH


class Line:
    def __init__(self, point1, point2) -> None:
        self.x = point1
        self.y = point2

    def draw(self, canvas, color):
        canvas.create_line(self.x.x, self.x.y, self.y.x,
                           self.y.y, fill=color, width=2)
        canvas.pack(fill=BOTH, expand=1)

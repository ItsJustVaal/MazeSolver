import time
from cells import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for x in range(self.num_cols):
            cells = []
            for y in range(self.num_rows):
                cells.append(Cell(self.win))
            self.cells.append(cells)
        for x in range(self.num_cols):
            for y in range(self.num_rows):
                self._draw_cell(x, y)

    def _draw_cell(self, x, y):
        if self.win is None:
            return
        x1 = self.x1 + x * self.cell_size_x
        y1 = self.y1 + y * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.cells[x][y].draw(x1, y1, x2, y2)
        self.animate()

    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        # time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self.cells[0][0].top = False
        self._draw_cell(0, 0)
        self.cells[self.num_cols - 1][self.num_rows - 1].bottom = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

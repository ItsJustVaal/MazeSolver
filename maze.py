import time
from cells import Cell
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visisted()

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

    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            listToVisit = []

            # left
            if i > 0 and not self.cells[i - 1][j].visited:
                listToVisit.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self.cells[i+1][j].visited:
                listToVisit.append((i + 1, j))
            # up
            if j > 0 and not self.cells[i][j - 1].visited:
                listToVisit.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
                listToVisit.append((i, j + 1))

            if len(listToVisit) == 0:
                self._draw_cell(i, j)
                return

            # random path
            direction = random.randrange(len(listToVisit))
            nextIndex = listToVisit[direction]

            # right
            if nextIndex[0] == i + 1:
                self.cells[i][j].right = False
                self.cells[i + 1][j].left = False
            # left
            if nextIndex[0] == i - 1:
                self.cells[i][j].left = False
                self.cells[i - 1][j].right = False
            # down
            if nextIndex[1] == j + 1:
                self.cells[i][j].bottom = False
                self.cells[i][j + 1].top = False
            # up
            if nextIndex[1] == j - 1:
                self.cells[i][j].top = False
                self.cells[i][j - 1].bottom = False

            self._break_walls_r(nextIndex[0], nextIndex[1])

    def _reset_cells_visisted(self):
        for x in self.cells:
            for y in x:
                y.visited = False

    def _solve_r(self, i, j):
        self.animate()

        self.cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        if i > 0 and not self.cells[i][j].left and not self.cells[i - 1][j].visited:
            self.cells[i][j].draw_move(self.cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i - 1][j], True)

        if i < self.num_cols - 1 and not self.cells[i][j].right and not self.cells[i + 1][j].visited:
            self.cells[i][j].draw_move(self.cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i + 1][j], True)

        if j > 0 and not self.cells[i][j].top and not self.cells[i][j - 1].visited:
            self.cells[i][j].draw_move(self.cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j - 1], True)

        if j < self.num_rows - 1 and not self.cells[i][j].bottom and not self.cells[i][j + 1].visited:
            self.cells[i][j].draw_move(self.cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j + 1], True)

        return False

    def solve(self):
        return self._solve_r(0, 0)

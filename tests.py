import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 18
        num_rows = 14
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1.cells[0][0].top, False,)
        self.assertEqual(m1.cells[num_cols - 1][num_rows - 1].bottom, False,)

    def test_reset_cells_visisted(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for x in m1.cells:
            for y in x:
                self.assertEqual(y.visited, False)


if __name__ == "__main__":
    unittest.main()

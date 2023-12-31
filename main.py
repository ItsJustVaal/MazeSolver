from maze import Maze
from window import Window


def main():
    num_rows = 12
    num_cols = 16
    margin = 10
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    window = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols,
                cell_size_x, cell_size_y, window)

    print("Maze Created")
    solvable = maze.solve()
    print(solvable)
    if not solvable:
        print("Maze cannot be solved")
    else:
        print("Maze solved!")

    window.wait_for_close()


main()

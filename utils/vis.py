def show_grid(grid):
    for row in grid:
        print(row)
    print()
def print_maze(maze):
    """Print the maze in a readable format."""
    for row in maze:
        print(' '.join(row))
    print()

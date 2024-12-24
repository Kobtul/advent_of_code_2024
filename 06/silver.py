from utils.advent_input_parser import parse_grid
from utils.vis import print_maze

with open('06/input.txt', 'r') as file:
    text = file.read()

maze = parse_grid(text)
print_maze(maze)



# Movement rules based on robot direction
MOVEMENTS = {
    '^': (-1, 0),  # Move up
    'v': (1, 0),   # Move down
    '<': (0, -1),  # Move left
    '>': (0, 1)    # Move right
}

DIRECTIONS = ['^', '>', 'v', '<']
def turn_right(current_direction):
    """Turn the robot 90° to the right."""
    current_index = DIRECTIONS.index(current_direction)
    return DIRECTIONS[(current_index + 1) % len(DIRECTIONS)]

def find_robot(maze):
    """Find the robot's location and direction in the maze."""
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell in MOVEMENTS: 
                return (row_idx, col_idx, cell)
    return None

def update_robot_location(maze,robot=None):
    """Update the robot's location based on its direction."""
    if not robot:
        robot = find_robot(maze)
    if not robot:
        print("No robot found!")
        return maze
    
    row, col, direction = robot
    d_row, d_col = MOVEMENTS[direction]  # Movement vector
    
    # New location test
    test_row = row + d_row
    test_col = col + d_col

    # Check if the move is within bounds and not hitting an obstacle
    if 0 <= test_row < len(maze) and 0 <= test_col < len(maze[0]):
        if maze[test_row][test_col] != '#':
            # Update the maze
            maze[row][col] = 'X'  # add visited symbol
            maze[test_row][test_col] = direction  # Move robot
            new_row = test_row
            new_col = test_col
            new_direction = direction
        elif maze[test_row][test_col] == '#':
            # rotate the robot
            new_direction = turn_right(direction)
            maze[row][col] = new_direction
            new_row = row
            new_col = col
        else:
            return maze,False,None

    else:
        return maze,False, None
    
    return maze,True,(new_row,new_col,new_direction) # second argument is if maze changed #third new robot loc



i=0
changed = True
location = None
while changed:
    print(f"Maze After {i} Move:")
    # print_maze(maze)
    maze,changed, location = update_robot_location(maze,location)
    i+=1


total_X = sum(row.count('X') for row in maze)
print(total_X + 1) # robots last location


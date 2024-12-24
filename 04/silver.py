from utils.advent_input_parser import parse_grid
from collections import defaultdict
import sys
import re

def rotate_45_degrees(orig_matrix):
    matrix = orig_matrix.copy()
    diagonals = defaultdict(list)
    # Group elements by the sum of their indices
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            diagonals[i + j].append(matrix[i][j])

    # Extract the groups in order
    return [diagonals[key] for key in sorted(diagonals.keys())]
def rotate_minus_45_degrees(orig_matrix):
    matrix = orig_matrix.copy()
    diagonals = defaultdict(list)
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # Group elements by the difference of their indices
    for i in range(num_rows):
        for j in range(num_cols):
            diagonals[i - j].append(matrix[i][j])

    # Extract the groups in order
    return [diagonals[key] for key in sorted(diagonals.keys(), reverse=True)]

def rotate_90_degrees(orig_matrix):
    # Transpose and reverse rows
    return [list(row)[::-1] for row in zip(*orig_matrix)]

def print_rotation(matrix):
    for row in matrix:
        print(row)
    print()

with open('04/input.txt', 'r') as file:
    text = file.read()
grid = parse_grid(text)
pattern = r"XMAS"


# print_rotation(transpose_minus_45_degrees(grid))
# list of rotations, starting 0,45 ending 315
# sys.exit(1)

rotations = []
rotations.append(grid)
grid_45 = rotate_45_degrees(grid)
rotations.append(grid_45)
grid_90 = rotate_90_degrees(grid)
rotations.append(grid_90)
grid_135 = rotate_45_degrees(grid_90)
rotations.append(grid_135)
grid_180 = rotate_90_degrees(grid_90)
rotations.append(grid_180)
grid_225 = rotate_45_degrees(grid_180)
rotations.append(grid_225)
grid_270 = rotate_90_degrees(grid_180)
rotations.append(grid_270)
grid_315 = rotate_45_degrees(grid_270)
rotations.append(grid_315)

def check_if_rotation_same(rotations):
    for i in range(len(rotations)):
        for j in range(len(rotations)):
            if i != j:
                if rotations[i] == rotations[j]:
                    print(f"Rotation {i * 45}° is the same as Rotation {j * 45}°")
print(check_if_rotation_same(rotations))

if False:
    for i, rotation in enumerate(rotations):
        print(f"Rotation {i * 45}°:")
        for row in rotation:
            print(row)
        print()

num_matches = 0

for i, rotation in enumerate(rotations):
    rot_matches = 0
    for row in rotation:
        strow = ''.join(row)
        rot_matches+= len(re.findall(pattern, strow))
    print(f"Rotation {i * 45}°: matches: {rot_matches}")

    num_matches+=rot_matches



print(num_matches)
# rotations = all_8_rotations(grid)


# if True:
#     for i, rotation in enumerate(rotations):
#         print(f"Rotation {i * 45}°:")
#         for row in rotation:
#             print(row)
#         print()

# num_matches = 0

# for i, rotation in enumerate(rotations):
#     rot_matches = 0
#     for row in rotation:
#         strow = ''.join(row)
#         rot_matches+= len(re.findall(pattern, strow))
#     print(f"Rotation {i * 45}°: matches: {rot_matches}")

#     num_matches+=rot_matches



# print(num_matches)

# # Example Usage
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# rotations = all_8_rotations(matrix)

# for i, rotation in enumerate(rotations):
#     print(f"Rotation {i * 45}°:")
#     for row in rotation:
#         print(row)
#     print()

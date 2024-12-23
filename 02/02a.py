# 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
# 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
# 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
# 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
# 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
# 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

# 

from utils.advent_input_parser import split_by_empty_lines

# load input.txt
with open('02a/input.txt', 'r') as file:
    lines = file.read().splitlines()
print(lines[:1])

number_of_safe_reports = 0
for line in lines:
    line = line.split()
    line = list(map(int, line))
    if line[0] < line[1]:
        incr = [1,2,3]
    else:
        incr = [-1,-2,-3]
    for i in range(len(line)-1):
        if not ((line[i+1] - line[i]) in incr):
            print('Unsafe')
            break
    else:
        number_of_safe_reports+=1
print(number_of_safe_reports)

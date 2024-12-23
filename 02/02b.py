# 7 6 4 2 1: Safe without removing any level.
# 1 2 7 8 9: Unsafe regardless of which level is removed.
# 9 7 6 2 1: Unsafe regardless of which level is removed.
# 1 3 2 4 5: Safe by removing the second level, 3.
# 8 6 4 4 1: Safe by removing the third level, 4.
# 1 3 6 7 9: Safe without removing any level.
# 

from utils.advent_input_parser import split_by_empty_lines

# load input.txt
with open('02a/input.txt', 'r') as file:
    lines = file.read().splitlines()
print(lines[:1])

def validate_list(my_list):
    if my_list[0] < my_list[1]:
        incr = [1,2,3]
    else:
        incr = [-1,-2,-3]
    for i in range(len(my_list)-1):
        if not ((my_list[i+1] - my_list[i]) in incr):
            return False
    else:
        return True

number_of_safe_reports = 0
for line in lines:
    line = line.split()
    line = list(map(int, line))
    if validate_list(line):
        number_of_safe_reports += 1
    else:
        for j in range(len(line)):
            new_line = line.copy()
            new_line.pop(j)
            if validate_list(new_line):
                number_of_safe_reports +=1
                break
    
print(number_of_safe_reports)
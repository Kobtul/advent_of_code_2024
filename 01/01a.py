from utils.advent_input_parser import parse_two_lists

# load input.txt
with open('01a/input.txt', 'r') as file:
    first, second = parse_two_lists(file.read())

# naive solution
# find a min value in the first list and second list
# and calculate distance between them
# remove min value from the list and repeat until one of the list is empty

def mm_distance(first, second):
    distance = 0
    while first and second:
        distance += abs(first.pop(first.index(min(first))) - second.pop(second.index(min(second))))
    return distance
print(mm_distance(first.copy(), second.copy()))
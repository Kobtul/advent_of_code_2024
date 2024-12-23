from utils.advent_input_parser import parse_two_lists

# load input.txt
with open('01a/input.txt', 'r') as file:
    first, second = parse_two_lists(file.read())

# naive solution
suma=0
for i in range(len(first)):
    for j in range(len(second)):
        if first[i] == second[j]:
            suma+=second[j]
print(suma)

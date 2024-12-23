# load input.txt
import re

with open('03/input.txt', 'r') as file:
    text = file.read()


pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

def mul(a, b):
    return a * b 

matches = re.findall(pattern, text)

all_mults = 0

# Evaluate the function for each match
for match in matches:
    a, b = map(int, match) 
    result = mul(a, b)  
    # print(f"fnc({a},{b}) = {result}")
    all_mults+=result
print(all_mults)

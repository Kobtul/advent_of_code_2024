# # Find matches and their locations
# for match in re.finditer(pattern, text):
#     start, end = match.span()  # Get the start and end positions of the match
#     matched_text = match.group()  # Get the matched text
#     print(f"Matched: {matched_text} at position: {start}-{end}")


# load input.txt
import re

with open('03/input.txt', 'r') as file:
    text = file.read()


pattern_mul = r"mul\((\d{1,3}),(\d{1,3})\)"
pattern_do = r"do\(\)"
pattern_dont = r"don't\(\)"


current_do = True

all_mults = 0

while True:
    closest_do = next(re.finditer(pattern_do,text), None)
    closest_dont = next(re.finditer(pattern_dont,text), None)
    closest_mul = next(re.finditer(pattern_mul,text), None)

    if closest_mul is None:
        break
    if closest_do is None and not current_do:
        break
    
    mul_start = closest_mul.span()[0]
    if closest_do is not None:
        do_start = closest_do.span()[0]
    else:
        do_start = len(text)
    if closest_dont is not None:
        dont_start = closest_dont.span()[0]
    else:
        dont_start = len(text)


    if do_start < dont_start and do_start < mul_start:
        current_do = True
        text = text[closest_do.span()[1]:]
    elif dont_start < do_start and dont_start < mul_start:
        current_do = False
        text = text[closest_dont.span()[1]:]
    else:
        if current_do:
            matched_text = closest_mul.group()
            match = re.findall(pattern_mul, matched_text)[0]

            a, b = map(int, match) 
            result = a*b  
            all_mults += result

        text = text[closest_mul.span()[1]:]
print(all_mults)





# def mul(a, b):
#     return a * b 

# matches = re.findall(pattern, text)

# all_mults = 0

# # Evaluate the function for each match
# for match in matches:
#     a, b = map(int, match) 
#     result = mul(a, b)  
#     # print(f"fnc({a},{b}) = {result}")
#     all_mults+=result
# print(all_mults)

from utils.advent_input_parser import split_by_empty_lines,parse_integers,parse_strings

with open('05/input.txt', 'r') as file:
    text = file.read()

text_sp = split_by_empty_lines(text)
rulez = text_sp[0]
seq = text_sp[1]


# this solution for every sequence it creates the dict from sequence where key is sequence number and value is position
# Afterwards it checks every rule, it gets position from dict and check if the rule holds
# because rulez form Partially ordered set, so switching elements in list according to rulez is finite(converging)

rulez_l = [tuple(map(int, line.split("|"))) for line in rulez.strip().split("\n")]

# print(rulez_l)
# print(seq)

def check_rulez(sq,sq_dict,rulez_l):
    was_changed = False
    while True: # for correcting rulez
        for x,y in rulez_l:
            pos_x = sq_dict.get(x, None)
            pos_y = sq_dict.get(y, None)
            if pos_x is None or pos_y is None:
                continue
            if pos_x >= pos_y:
                # switching places in sequence to fix it
                was_changed = True
                pm = sq[pos_x]
                sq[pos_x] = sq[pos_y]
                sq[pos_y] = pm

                pm = sq_dict[x]
                sq_dict[x] = sq_dict[y]
                sq_dict[y] = pm

                break
        else:
            break
        
    # get middle number
    if was_changed:
        return sq[(len(sq)-1)//2]
    else:
        return 0


seq_l = [list(map(int,x.split(','))) for x in parse_strings(seq)]
res = 0
for sq in seq_l:
    sq_dict = {value:index for index, value in enumerate(sq)}
    res+=check_rulez(sq,sq_dict,rulez_l)
print(res)


# print(seq)


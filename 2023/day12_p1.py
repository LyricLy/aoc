from common import *
a = get_input()

def get_nums(s):
    return [len(x) for x in s.replace(".", " ").split()]

def get_hand_type(x, y):
    posses = [""]
    for c in x:
        new_posses = []
        for pos in posses:
            if c == "?":
                for ccc in ".#":
                    new_posses.append(pos + ccc)
            else:
                new_posses.append(pos + c)
        posses = new_posses
    return sum(1 for p in posses if get_nums(p) == y)

c = 0
for line in a:
    a, b = line.split(" ")
    c += get_hand_type(a.string, b.nums)
print(c)


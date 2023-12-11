from common import *
from itertools import cycle
from math import lcm

a = get_input()

s = a[0]

m = {k.string: v.string.strip("()").split(", ") for k, v in a[1]}

cycles = []

for state in m.keys():
    if not state.endswith("A"):
        continue
    aaa = 1
    for c in cycle(s.string):
        state = m[state][c == "R"]
        if state.endswith("Z"):
            break
        aaa += 1
    cycles.append(aaa)

print(lcm(*cycles))

from common import *
from itertools import cycle
a = get_input()

s = a[0]

m = {k: v.string.strip("()").split(", ") for k, v in a[1]}

state = "AAA"

aaa = 1
for c in cycle(s.string):
    state = m[state][c == "R"]
    if state == "ZZZ":
        break
    aaa += 1
print(aaa)

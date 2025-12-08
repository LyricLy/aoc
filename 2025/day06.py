import math
from itertools import zip_longest
from common import *
a = get_input()
a.string = " " + a.string  # LOL

steps = [i for i, x in enumerate(a[-1].string) if x != " "]

c = 0
for i, column in enumerate(steps[1:] + [len(a.string.splitlines()[0])+1]):
    r = [int("".join(s)) for s in zip(*[t[steps[i]:column-1] for t in a.string.splitlines()[:-1]])]
    if a[-1].string[steps[i]] == "*":
        c += math.prod(r)
    else:
        c += sum(r)
print(c)

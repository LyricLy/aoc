from common import *
import itertools
import math
a = get_input()

def extrapolate(n):
    if set(n) == {0}:
        return 0
    ts = []
    for i, x in enumerate(n[1:], 1):
        ts.append(x-n[i-1])
    return n[0] - extrapolate(ts)

c = 0
for b in a:
    c += extrapolate(b.nums)
print(c)

from common import *
import itertools
import functools
a = get_input()

reqs = {tuple(x) for x in a[0]}

def the_cmper(x, y):
    if (x, y) in reqs:
        return 1
    elif (y, x) in reqs:
        return -1
    else:
        return 0

c = 0
for thing in a[1]:
    if any((counter := p[::-1]) in reqs for p in itertools.combinations(thing, 2)):
        t = sorted(thing.nums, key=functools.cmp_to_key(the_cmper))
        c += t[len(t)//2]
print(c)

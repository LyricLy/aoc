from common import *
import itertools
a = get_input()

reqs = {tuple(x) for x in a[0]}

c = 0
for thing in a[1]:
    if not any((counter := p[::-1]) in reqs for p in itertools.combinations(thing, 2)):
        c += thing.nums[len(thing.nums)//2]
print(c)

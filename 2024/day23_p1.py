from common import *
from collections import defaultdict
a = get_input()

d = defaultdict(list)
for x, y in a:
    d[x.string].append(y.string)
    d[y.string].append(x.string)

c = 0
for x in d:
    for y in d[x]:
        for z in d[y]:
            for w in d[z]:
                if x == w and "t" in (x+y+z)[::2]:
                    c += 1
print(c // 6)

example = 0
with open("example.txt" if example else "input.txt") as f:
    t = f.read()

import re
import itertools
beacons = [tuple(map(int, x)) for x in re.findall(r"Sensor at x=(\d+), y=(\d+): closest beacon is at x=(\d+), y=(\d+)", t)]

X = 4000000+1

dead_ranges = [[] for _ in range(X)]
for (x, y, bx, by) in beacons:
    d = abs(x-bx)+abs(y-by)
    for n in range(y-d, y+d+1):
        start = x-d+abs(y-n)
        if 0 <= n < X:
            dead_ranges[n].append(range(start, start+max(d*2+1-abs(y-n)*2, 0)))

def unify(x, y):
    if y.start < x.start:
        x, y = y, x
    if x.stop > y.stop:
        return x
    if y.start < x.stop:
        return range(x.start, y.stop)
    return None

def fix_ranges(dr):
    dr.sort(key=lambda n: n.start)
    l = [dr[0]]
    for r in dr[1:]:
        if u := unify(r, l[-1]):
            l.pop()
            l.append(u)
        else:
            l.append(r)
    return l
        

for (y, dr) in enumerate(dead_ranges):
    if len(a := fix_ranges(dr)) > 1:
        print(y, a)

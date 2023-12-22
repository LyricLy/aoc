from common import *
from collections import defaultdict
a = get_input()

bottom_levels = defaultdict(list)
top_levels = defaultdict(list)

class Point:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

    def overlaps(self, other):
        return self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1

    def drop(self):
        p = 0
        while self.z1 - p > 1 and not any(self.overlaps(x) for x in top_levels[self.z1-p-1]):
            p += 1
        if p:
            top_levels[self.z2].remove(self)
            bottom_levels[self.z1].remove(self)
            self.z2 -= p
            self.z1 -= p
            top_levels[self.z2].append(self)
            bottom_levels[self.z1].append(self)

    def __repr__(self):
        return f"{self.x1},{self.y1},{self.z1}~{self.x2},{self.y2},{self.z2}"

for l in a:
    h, j = l.split("~")
    x1, y1, z1 = h.nums
    x2, y2, z2 = j.nums
    x1, x2 = sorted((x1, x2))
    y1, y2 = sorted((y1, y2))
    z1, z2 = sorted((z1, z2))
    p = Point(x1, y1, z1, x2, y2, z2)
    top_levels[z2].append(p)
    bottom_levels[z1].append(p)

for _, ts in sorted(top_levels.items()):
    for t in ts[:]:
        t.drop()

s = set()
for i, ts in bottom_levels.items():
    for t in ts:
        ll = [x for x in top_levels[i-1] if t.overlaps(x)]
        if len(ll) == 1:
            s.add(ll[0])
print(len(a) - len(s))

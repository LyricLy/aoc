from common import *
import functools
a = get_input()

def meets_mask(p, mask):
    return all(c == "?" or k == c for k, c in zip(p, mask))

def places_meeting_mask(r, mask, dot_count):
    for i in range(len(mask)-r+1):
        if meets_mask("."*i+"#"*r+"."*dot_count, mask):
            yield i

@functools.cache
def ways(p, mask):
    if p[0] > len(mask):
        return 0
    if len(p) == 1:
        return sum(1 for _ in places_meeting_mask(p[0], mask, len(mask)))
    xs = 0
    for i in places_meeting_mask(p[0], mask, 1):
        xs += ways(p[1:], mask[p[0] + i + 1:])
    return xs

points = 0
for row in a:
    x, y = row.split(" ")
    a, b = ((x.string+"?")*5)[:-1], y.nums*5
    points += ways(tuple(b), a)
print(points)

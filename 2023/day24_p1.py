from common import *
import itertools
a = get_input()
hailstones = []
for l in a:
    x, y = l.split("@")
    hailstones.append((x.nums, y.nums))

c = 0
for ((x1, y1, _), (dx1, dy1, _)), ((x2, y2, _), (dx2, dy2, _)) in itertools.combinations(hailstones, r=2):
    x1, y1, x2, y2, x3, y3, x4, y4 = x1, y1, x1+dx1, y1+dy1, x2, y2, x2+dx2, y2+dy2
    try:
        px = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
        py = ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    except ZeroDivisionError:
        continue

    is_broken = False
    for p, coord, d in [(px, x1, dx1), (py, y1, dy1), (px, x3, dx2), (py, y3, dy2)]:
        if d < 0:
            is_broken = is_broken or p > coord
        else:
            is_broken = is_broken or p < coord
    if is_broken:
        continue
    if 200000000000000 <= px <= 400000000000000 and 200000000000000 <= py <= 400000000000000:
        c += 1
print(c)

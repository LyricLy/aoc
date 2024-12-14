from common import *
from collections import defaultdict
a = get_input()

d = {(a, b): 0 for x in a for a, b, c, d in [x.nums]}
g = Grid.from_dict(defaultdict(lambda: 0, d))
width = g.width
height = g.height

TIMES = 100

for robot in a:
    x, y, dx, dy = robot.nums
    g[(x+dx*TIMES)%width, (y+dy*TIMES)%height] += 1

quadrants = Grid(2, 2, 0)

for p in g:
    if width % 2 and p[0] == width // 2 or height % 2 and p[1] == height // 2:
        continue
    quadrant = p[0] // (width // 2 + 1), p[1] // (height // 2 + 1)
    quadrants[quadrant] += g[p]

c = 1
for n in quadrants.values():
    c *= n
print(c)


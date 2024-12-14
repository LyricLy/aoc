from common import *
from collections import defaultdict
import math
from tqdm import tqdm
a = get_input()

d = {(a, b): 0 for x in a for a, b, c, d in [x.nums]}
core = Grid.from_dict(defaultdict(lambda: 0, d))
width = core.width
height = core.height

TIMES = 10403

def cycles_for(dx, width):
    c = 0
    i = 0
    while True:
        i += 1
        c += dx
        c %= width
        if c == 0:
            break
    return i

scores = []

for TIMES in tqdm(range(0, 10403)):
    g = core.copy()
    for robot in a:
        x, y, dx, dy = robot.nums
        g[(x+dx*TIMES)%width, (y+dy*TIMES)%height] += 1

    quadrants = Grid(3, 3, 0)
    for p in g:
        quadrant = p[0] // (width // 3 + 1), p[1] // (height // 3 + 1)
        quadrants[quadrant] += g[p]
    score = quadrants[1, 1]

    scores.append((score, TIMES))

print(max(scores, key=lambda x: x[0])[1])

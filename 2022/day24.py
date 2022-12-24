import math
from common import orthagonals, offset
from collections import deque

example = 0

with open("example.txt" if example else "input.txt") as f:
    t = f.read()

grid = t.splitlines()

width = len(grid[0])-2
height = len(grid)-2

rows = [[] for _ in range(height)]
cols = [[] for _ in range(width)]

for y in range(height):
    for x in range(width):
        match grid[y+1][x+1]:
            case "^":
                cols[x].append((-1, y))
            case "v":
                cols[x].append((1, y))
            case ">":
                rows[y].append((1, x))
            case "<":
                rows[y].append((-1, x))

def is_safe(x, y, t):
    for m, n in cols[x]:
        if (n+m*t)%height == y:
            return False
    for m, n in rows[y]:
        if (n+m*t)%width == x:
            return False
    return True

def in_range(x, y):
    return 0 <= x < width and 0 <= y < height

def next_stage(x, y, stage):
    if stage % 2 == 0:
        return stage + ((x, y) == (width-1, height))
    else:
        return stage + ((x, y) == (0, -1))

repeats = math.lcm(height, width)

answers = {(0, -1, 0, 0): 0}
frontier = deque([(0, -1, 0, 0)])
while frontier:
    x, y, t, stage = frontier.popleft()
    next_t = (t+1) % repeats
    for d in orthagonals + [(0, 0)]:
        xx, yy = offset(x, y, d)
        sstage = next_stage(xx, yy, stage)
        if sstage == 3:
            print(answers[x, y, t, stage] + 1)
            exit(0)
        if (xx, yy, next_t, sstage) in answers or (xx, yy) not in ((0, -1), (width-1, height)) and (not in_range(xx, yy) or not is_safe(xx, yy, next_t)):
            continue
        answers[xx, yy, next_t, sstage] = answers[x, y, t, stage] + 1
        frontier.append((xx, yy, next_t, sstage))

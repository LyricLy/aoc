with open("input.txt") as f:
    t = f.read()

d = set()

def plus1_latest(s):
    x, y = s
    return x, y+1

for path in t.splitlines():
    path = path.split(" -> ")
    s = eval(path[0])
    for coord in path[1:]:
        coord = eval(coord)
        for x in range(*plus1_latest(sorted([coord[0], s[0]]))):
            for y in range(*plus1_latest(sorted([coord[1], s[1]]))):
                d.add((x, y))
        s = coord

abyss = max(y for (x, y) in d)+2
from common import offset, Grid

def print_d():
    print("===")
    left = min(x for (x, y) in d)
    right = max(x for (x, y) in d)
    top = min(y for (x, y) in d)
    bottom = max(y for (x, y) in d)
    grid = Grid(right-left+1, bottom-top+1, " ")
    for p in d:
        grid[offset(p, (-left, -top))] = "#"
    print(grid)

c = 0
while True:
    sand = 500, 0
    if sand in d:
        print(c)
        break
    while True:
        for cand in ((0, 1), (-1, 1), (1, 1)):
            o = offset(sand, cand)
            if o not in d and o[1] < abyss:
                sand = o
                break
        else:
            d.add(sand)
            c += 1
            break

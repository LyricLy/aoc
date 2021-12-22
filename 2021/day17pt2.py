from common import *

with open("input.txt") as f:
    t = f.read()

xx, xxx = map(int, t.split(": ")[1].split(", ")[0].split("=")[1].split(".."))
xxx += 1
x = range(xx, xxx)
yy, yyy = map(int, t.split(": ")[1].split(", ")[1].split("=")[1].split(".."))
yyy += 1
y = range(yy, yyy)

def try_traj(dx, dy):
    maxy = 0
    cx, cy = 0, 0
    while (cx < x.stop if dx > 0 else cx >= x.start if dx < 0 else True) and (True if dy > 0 else cy >= y.start if dy < 0 else True):
        cx += dx
        cy += dy
        if cy > maxy:
            maxy = cy
        if cx in x and cy in y:
            return True
        dy -= 1
        dx += (-1 if dx > 0 else 1 if dx < 0 else 0)
    return False

c = 0
for dx, dy in ((dx, dy) for dy in range(-300, 301) for dx in range(-300, 301)):
    if try_traj(dx, dy):
        c += 1
print(c)

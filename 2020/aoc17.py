with open("test.txt") as f:
    data = f.read()

from collections import defaultdict
cubes = defaultdict(bool)

for yi, y in enumerate(data.splitlines()):
    for xi, x in enumerate(y):
        if x == "#":
            cubes[(xi, yi, 0)] = True
xl = [0, len(data.splitlines())-1]
yl = [0, len(data.splitlines()[0])-1]
zl = [0, 0]

def print_config():
    for z in range(zl[0], zl[1]+1):
        print(f"z={z}")
        for y in range(yl[0], yl[1]+1):
            for x in range(xl[0], xl[1]+1):
                print(".#"[cubes[(x, y, z)]], end="")
            print()
        print()

import itertools
def do_step():
    global cubes
    ccubes = cubes.copy()
    for x, y, z in itertools.product(range(xl[0]-1, xl[1]+2), range(yl[0]-1, yl[1]+2), range(zl[0]-1, zl[1]+2)):
        neighbors = sum(cubes[(x+dx, y+dy, z+dz)] for dx, dy, dz in itertools.product(range(-1, 2), range(-1, 2), range(-1, 2)) if dx or dy or dz)
        if cubes[(x, y, z)] and neighbors not in (2, 3):
            ccubes[(x, y, z)] = False
        elif not cubes[(x, y, z)] and neighbors == 3:
            ccubes[(x, y, z)] = True
            if x > xl[1]:
                xl[1] = x
            elif x < xl[0]:
                xl[0] = x
            if y > yl[1]:
                yl[1] = y
            elif y < yl[0]:
                yl[0] = y
            if z > zl[1]:
                zl[1] = z
            elif z < zl[0]:
                zl[0] = z
    cubes = ccubes
    

for _ in range(6):
    do_step()
    print("\n===")
print_config()

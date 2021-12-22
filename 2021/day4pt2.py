with open("input.txt") as f:
    i = f.read()

import itertools
ns = [int(x) for x in i.splitlines()[0].split(",")]
grids = [([[[int(y), False] for y in x.split()] for x in g.split("\n")], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]) for g in i.split("\n\n")[1:]]
U = len(grids)
for n in ns:
    for grid in grids:
        won = False
        for x, y in itertools.product(range(5), range(5)):
            if grid[0][y][x][0] == n:
                grid[0][y][x][1] = True
                grid[1][x] += 1
                if grid[1][x] == 5:
                    won = True
                grid[2][y] += 1
                if grid[2][y] == 5:
                    won = True
        print(len(grid[0]))
        print("\n".join(" ".join(str(x) for x in y) for y in grid[0]))
        if won:
            U -= 1
            for x, y in itertools.product(range(5), range(5)):
                grid[1][x] = -999999999
                grid[2][y] = -999999999
            if U == 0:
                s = 0
                for x, y in itertools.product(range(5), range(5)):
                    if not grid[0][y][x][1]:
                        s += grid[0][y][x][0]
                print(s * n)
                
                exit(0)
                print(s * n)

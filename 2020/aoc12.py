def parse_direction(t):
    return t[0], int(t[1:])

with open("input.txt") as f:
    data = [*map(parse_direction, f.readlines())]

dir = 0
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y = 0, 0
nx, ny = 10, -1

for c, n in data:
    print(x, y)
    if c == "F":
        x += nx * n
        y += ny * n
    elif c in "ESWN":
        i = "ESWN".index(c)
        dx, dy = DIRS[i]
        nx += dx * n
        ny += dy * n
    else:
        d = 1 if c == "R" else -1
        d *= n // 90
        print(nx, ny)
        for _ in range(d % 4):
            pxn = ny * -1
            pyn = nx
            ny = pyn
            nx = pxn
        print(nx, ny)

print(abs(x) + abs(y))

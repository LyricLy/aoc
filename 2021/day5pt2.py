with open("input.txt") as f:
    i = f.read().strip().splitlines()

def ize(x, y):
    l = [x, y]
    l.sort()
    l[1] += 1
    return l

k = [[[*map(int, x.strip().split(","))] for x in l.split("->")] for l in i]
grid = [[0 for _ in range(1000)] for _ in range(1000)]
for line in k:
    p1, p2 = line
    if p1[0] == p2[0]:
        x = p1[0]
        for y in range(*ize(p1[1], p2[1])):
            grid[y][x] += 1
    elif p1[1] == p2[1]:
        y = p1[1]
        for x in range(*ize(p1[0], p2[0])):
            grid[y][x] += 1
    elif p1[0] - p2[0] == p1[1] - p2[1] or p1[0] - p2[0] == -(p1[1] - p2[1]):
        x = p1[0]
        y = p1[1]
        while True:
            grid[y][x] += 1
            if [x, y] == p2:
                break
            if x < p2[0]:
                x += 1
            else:
                x -= 1
            if y < p2[1]:
                y += 1
            else:
                y -= 1

c = 0
for row in grid:
    for e in row:
        if e >= 2:
            c += 1
print("\n".join("".join(str(x) for x in g) for g in grid))
print(c)

example = 0

with open("example.txt" if example else "input.txt") as f:
    t = f.read()

import re
from common import Grid, orthagonals

m, t = t.split("\n\n")
lines = m.splitlines()
max_len = max(len(s) for s in lines)
g = Grid.parse("\n".join(f"{s:<{max_len}}" for s in lines), lambda s: s)

xxx = 0
while g[xxx, 0] != ".":
    xxx += 1

pos = xxx, 0
facing = 1, 0

def get_section(pos):
    x, y = pos
    if 50 <= x < 100 and 0 <= y < 50:
        return 1
    if 100 <= x < 150 and 0 <= y < 50:
        return 2
    if 50 <= x < 100 and 50 <= y < 100:
        return 3
    if 0 <= x < 50 and 100 <= y < 150:
        return 4
    if 50 <= x < 100 and 100 <= y < 150:
        return 5
    if 0 <= x < 50 and 150 <= y < 200:
        return 6
    return None

def get_move(pos, move):
    x, y = pos
    dx, dy = move
    match get_section(pos):
        case 1 if y+dy < 0:
            return (0, x-50+150), (1, 0)
        case 1 if x+dx < 50:
            return (0, 49-y+100), (1, 0)

        case 2 if y+dy >= 50:
            return (99, x-100+50), (-1, 0)
        case 2 if y+dy < 0:
            return (x-100, 199), (0, -1)
        case 2 if x+dx >= 150:
            return (99, 49-y+100), (-1, 0)

        case 3 if x+dx < 50:
            return (y-50, 100), (0, 1)
        case 3 if x+dx >= 100:
            return (y-50+100, 49), (0, -1)

        case 4 if x+dx < 0:
            return (50, 149-y), (1, 0)
        case 4 if y+dy < 100:
            return (50, x+50), (1, 0)

        case 5 if x+dx >= 100:
            return (149, 149-y), (-1, 0)
        case 5 if y+dy >= 150:
            return (49, x-50+150), (-1, 0)

        case 6 if x+dx >= 50:
            return (y-150+50, 149), (0, -1)
        case 6 if x+dx < 0:
            return (y-150+50, 0), (0, 1)
        case 6 if y+dy >= 200:
            return (x+100, 0), (0, 1)

        case None:
            raise ValueError("what the hell")

        case _:
            return (x+dx, y+dy), move


for code in re.findall(r"\d+|[LR]", t):
    if code.isdigit():
        n = int(code)
        for _ in range(n):
            next_pos, next_facing = get_move(pos, facing)
            if g[next_pos] == "#":
                break
            pos, facing = next_pos, next_facing
    elif code == "R":
        dx, dy = facing
        facing = -dy, dx
    else:
        dx, dy = facing
        facing = dy, -dx

x, y = pos
x += 1
y += 1
f = (orthagonals.index(facing)-1) % 4
print(y*1000+x*4+f)

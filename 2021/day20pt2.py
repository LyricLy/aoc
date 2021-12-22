from common import *

with open("input.txt") as f:
    t = f.read()

f, g = t.split("\n\n")
g = Grid.parse(g, lambda x: x == "#")
d = {}
s = 0
for i in g:
    x, y = i
    d[i] = g[i]
    if max(i) > s:
        s = max(i)

default = False

def get_pos(pos):
    return d.get(pos, default)

def do_a_step():
    global d, default, s
    new_d = {}
    for y in range(-s-1, s+2):
        for x in range(-s-1, s+2):
            bn = ""
            for dx, dy in sorted(directions+[(0, 0)], key=lambda x: (x[1], x[0])):
                bn += str(int(get_pos((x+dx, y+dy))))
            new_d[(x, y)] = f[int(bn, 2)] == "#"
    if f[0] == "#" and default == False:
        default = True
    elif f[-1] == "." and default == True:
        default = False
    d = new_d
    s += 1

for i in range(50):
    do_a_step()
print(sum(d.values()))

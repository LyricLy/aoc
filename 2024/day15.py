from common import *
a = get_input()

og = a[0].grid
g = Grid(og.width * 2, og.height, ".")
for p in og:
    tl = p[0]*2, p[1]
    tr = offset(tl, (1, 0))
    match og[p]:
        case "#":
            g[tl], g[tr] = "##"
        case "O":
            g[tl], g[tr] = "[]"
        case "@":
            pos = tl

def can_move(p, d):
    match g[p]:
        case ".":
            return True
        case "#":
            return False
        case "[":
            l = can_move(offset(p, (0, d)), d)
            r = can_move(offset(p, (1, d)), d)
            return l and r
        case "]":
            l = can_move(offset(p, (-1, d)), d)
            r = can_move(offset(p, (0, d)), d)
            return l and r

def move(p, d):
    match g[p]:
        case "[":
            move(l := offset(p, (0, d)), d)
            move(r := offset(p, (1, d)), d)
            g[p] = "."
            g[offset(p, (1, 0))] = "."
            g[l] = "["
            g[r] = "]"
        case "]":
            move(l := offset(p, (-1, d)), d)
            move(r := offset(p, (0, d)), d)
            g[p] = "."
            g[offset(p, (-1, 0))] = "."
            g[l] = "["
            g[r] = "]"

moves = a[1].string
for c in moves:
    if not c.strip():
        continue
    d = orthogonals["^>v<".index(c)]
    if not d[1]:
        tp = pos
        moving = []
        while g[tp := offset(tp, d)] in "[]":
            moving.append(tp)
        if g[tp] == "#":
            continue
        for x in moving[::-1]:
            g[offset(x, d)] = g[x]
            g[x] = "."
    else:
        if not can_move(offset(pos, d), d[1]):
            continue
        move(offset(pos, d), d[1])
    pos = offset(pos, d)

print(g)
c = 0
for p in g:
    if g[p] == "[":
        c += p[0] + p[1]*100
print(c)

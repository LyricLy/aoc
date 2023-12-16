from common import *
a = get_input().grid
b = Grid(a.width, a.height, False)

ps = [((0, 0), (1, 0))]
seen = set()

while ps:
    p, d = ps.pop()
    while p in a and (p, d) not in seen:
        seen.add((p, d))
        b[p] = True
        x, y = d
        c = a[p]
        if c == "/":
            if x:
                d = (y, -x)
            else:
                d = (-y, x)
        elif c == "\\":
            if x:
                d = (-y, x)
            else:
                d = (y, -x)
        elif c == "|" and x or c == "-" and y:
            d = (y, -x)
            ps.append((p, (-y, x)))
        p = offset(p, d)

print(b.count(lambda x: x))

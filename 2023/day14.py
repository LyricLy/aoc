from common import *
a = get_input().grid

def move_in(d):
    if d == (0, -1):
        rr = a.columns()
    elif d == (0, 1):
        rr = [x[::-1] for x in a.columns()]
    elif d == (-1, 0):
        rr = a.rows()
    else:
        rr = [x[::-1] for x in a.rows()]
    for col in rr:
        for p in col:
            while a[p] == "O" and a[prev := offset(p, d)] == ".":
                a[prev] = "O"
                a[p] = "."
                p = prev

c = []
while True:
    copy = a.copy()
    try:
        i = c.index(copy)
        left = 1000000000 - len(c)
        r = c[i + (left % (len(c) - i))]
        break
    except ValueError:
        c.append(copy)
    for d in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        move_in(d)

c = 0
for x in r:
    if r[x] == "O":
        c += (r.height-x[1])
print(c)

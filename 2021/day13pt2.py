with open("input.txt") as f:
    t = f.read()
fst, snd = t.split("\n\n")
s = set(tuple(int(x) for x in y.split(",")) for y in fst.splitlines())

def do_fold(s, do_y, c):
    t = list(s)
    for x in t:
        ch = x[0] if not do_y else x[1]
        new = x
        if ch > c:
            n = c - (ch - c)
            if do_y:
                new = (x[0], n)
            else:
                new = (n, x[1])
        if new != x:
            s.remove(x)
            s.add(new)

def parse_fold(s):
    s = s.removeprefix("fold along ")
    if s[0] == "x":
        do_y = False
    else:
        do_y = True
    return (do_y, int(s[2:]))

for line in snd.splitlines():
    do_fold(s, *parse_fold(line))

mx, my = map(max, zip(*s))
mx += 1
my += 1

# kerning
i = 0
while i < mx:
    o = 0
    l = [(x, y) for x in range(i, mx) for y in range(0, my+1)]
    while True:
        ns = s.copy()
        for x, y in l:
            x -= o
            y -= o
            if (x, y) not in ns:
                continue
            if x-2<i and (x-2, y) in s or x<=0:
                break
            ns.remove((x, y))
            ns.add((x-1, y))
        else:
            s = ns
            o += 1
            continue
        break
    mx -= o
    i -= o
    i += 5

from rich import print
for y in range(my):
    for x in range(mx):
        if (x, y) in s:
            print("[cyan]██[/]", end="")
        else:
            print("  ", end="")
    print()

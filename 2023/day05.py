with open("input.txt") as f:
    r = f.read()

def digof(s):
    import re
    return [int(x) for x in re.findall("\d+", s)]

sections = r.split("\n\n")
root = digof(sections[0])
m = {}
for x in sections[1:]:
    fro, to = x.split("-")[0], x.split("-")[2].split()[0]
    a = []
    for l in x.strip().split("\n")[1:]:
        a.append(digof(l))
    m[fro] = (to, a)

def deoverlap(x, y):
    if x[0] <= y[0] and x[1] >= y[1]:
        return y, [(x[0], y[0]), (y[1], x[1])]
    if y[0] <= x[0] and y[1] >= x[1]:
        return x, []
    if x[1] > y[0] and x[0] <= y[0]:
        return (y[0], x[1]), [(x[0], y[0])]
    if y[1] > x[0] and y[0] <= x[0]:
        return (x[0], y[1]), [(y[1], x[1])]
    return (0, 0), [x]

type = "seed"
frontier = [(root[i], root[i] + root[i+1]) for i in range(0, len(root), 2)]

while type != "location":
    to, ttt = m[type]
    n = []
    for hh in frontier:
        for b, a, c in ttt:
            START = (a, a+c)
            CC, chaff = deoverlap(hh, START)
            if CC == (0, 0):
                continue
            for x in chaff:
                if x[0] != x[1]:
                    frontier.append(x)
            n.append(((CC[0] + (b-a)), (CC[1] + (b-a))))
            break
        else:
            n.append(hh)
    type = to
    frontier = n

print(min(frontier, key=lambda x: x[0]))

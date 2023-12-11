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

type = "seed"
frontier = root

while type != "location":
    to, ttt = m[type]
    n = []
    for x in frontier:
        for b, a, c in ttt:
            if x in range(a, a+c):
                n.append(x + b-a)
                break
        else:
            n.append(x)
    type = to
    frontier = n
print(min(frontier))


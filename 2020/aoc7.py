import re

class View:
    def __init__(self, s):
        self.s = s
        self.idx = 0

    def __getitem__(self, o):
        return self.s[self.idx:][o]

with open("input.txt") as f:
    input = f.read()

def parse_bag(v):
    return parse_off(v, r"(.*?) bags?").group(1)

def parse_off(v, r):
    m = re.match(r, v[:])
    try:
        v.idx += m.end()
    except AttributeError:
        print(v[:].splitlines()[0])
        raise
    return m

def do_thing(d):
    v = View(d)
    d = {}
    while v[:]:
        b = parse_bag(v)
        k = {}
        parse_off(v, " contain ")
        while v[0] not in ".n":
            c = int(parse_off(v, "(, )?(\d+) ").group(2))
            ba = parse_bag(v)
            k[ba] = c
        parse_off(v, "no other bags\.\n|\.\n")
        d[b] = k
    return d

t = do_thing(input)

def count_bags(s):
    b = t[s]
    if not b:
        return 0
    s = 0
    for c, v in b.items():
        s += count_bags(c) * v
        s += v
    return s

print(count_bags("shiny gold"))

from common import *
a = get_input()

any_all = [set(range(1, 4001)) for _ in range(4)]

def parse_cond(cond):
    if "<" in cond:
        x, y = cond.split("<")
        our = set(range(1, int(y)))
    else:
        x, y = cond.split(">")
        our = set(range(int(y)+1, 4001))
    match x:
        case "x":
            return our, set(range(1, 4001)), set(range(1, 4001)), set(range(1, 4001))
        case "m":
            return set(range(1, 4001)), our, set(range(1, 4001)), set(range(1, 4001))
        case "a":
            return set(range(1, 4001)), set(range(1, 4001)), our, set(range(1, 4001))
        case "s":
            return set(range(1, 4001)), set(range(1, 4001)), set(range(1, 4001)), our

import itertools
def constrict(sets, constriction):
    return tuple(itertools.starmap(set.intersection, zip(sets, constriction)))

def minus(sets, constriction):
    for x, y in zip(sets, constriction):
        if len(y) != 4000:
            x -= y

def parse_workflow(s):
    name, body = s.split("{", 1)
    cases = body.rstrip("}").split(",")
    cases = [(parse_cond((x := c.split(":"))[0]), x[1]) if ":" in c else (any_all, c) for c in cases]
    return name, cases

workflows = {}
for workflow in a[0]:
    name, cases = parse_workflow(workflow.string)
    workflows[name] = cases

import math
def parse_bad_dict(s):
    return eval(s.replace("=", ":"), {"x": "x", "m": "m", "a": "a", "s": "s"})

def accepts_of(workflow, sets):
    if not any(sets) or workflow == "R":
        return 0
    if workflow == "A":
        return math.prod(map(len, sets))
    t = 0
    for a, b in workflows[workflow]:
        t += accepts_of(b, constrict(sets, a))
        minus(sets, a)
    return t

print(accepts_of("in", any_all))

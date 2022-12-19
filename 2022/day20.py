example = 0

with open("example.txt" if example else "input.txt") as f:
    t = f.read()

import re
from dataclasses import dataclass

blueprints = [[(re.search("(\w+) robot", l)[1], {x[2]: int(x[1]) for x in re.finditer("(\d+) (\w+)", l)}) for l in ll.split(". ")] for ll in t.splitlines()]

from frozendict import frozendict
from functools import cache
import math

best_so_far = 0
maximums = [{mat: max(costs.get(mat, 0) for _, costs in blueprint) or math.inf for mat, _ in blueprint} for blueprint in blueprints]

@cache
def most_lucrative(p, r, tr, bp):
    global best_so_far

    # case: give up
    m = p.get("geode", 0) + tr*r.get("geode", 0)

    # is this path fucked?
    if m + tr*(tr+1)//2 <= best_so_far:
        return m

    for robot, costs in blueprints[bp]:
        if r.get(robot, 0) >= maximums[bp][robot]:
            continue
        # case: save up for and buy `robot`
        n = max(max(math.ceil((amount-p.get(item, 0)) / r[item]), 0) if item in r else math.inf for item, amount in costs.items())
        if n > tr:
            continue
        new_p = frozendict({k: p.get(k, 0) + (n+1)*v - costs.get(k, 0) for k, v in r.items()})
        new_r = r.set(robot, r.get(robot, 0) + 1)
        m = max(m, most_lucrative(new_p, new_r, tr-n-1, bp))
        best_so_far = max(best_so_far, m)

    return m

s = 1
for i in range(3):
    s *= most_lucrative(frozendict(), frozendict({"ore": 1}), 32, i)
    best_so_far = 0
print(s)

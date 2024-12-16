from common import *
from collections import defaultdict
import heapq
a = get_input().grid

start = a.extract("S", ".")
end = a.extract("E", ".")

costs = defaultdict(lambda: float("inf"))
pathss = {}
q = []

def new_plan(state, cost, paths):
    if cost < costs[state]:
        costs[state] = cost
        pathss[state] = paths
        heapq.heappush(q, (cost, state))
    elif cost == costs[state]:
        pathss[state].extend(paths)

new_plan((start, (1, 0)), 0, [[start]])

while q:
    _, (p, d) = heapq.heappop(q)

    if p == end:
        paths = pathss[(p, d)]
        s = set()
        for x in paths:
            s.update(x)
        print(len(s))

    # step forward
    new_p = offset(p, d)
    if a[new_p] == ".":
        new_plan((new_p, d), costs[p, d] + 1, [path + [new_p] for path in pathss[p, d]])

    # turn
    for new_d in [(-d[1], d[0]), (d[1], -d[0])]:
        new_cost = costs[(p, d)] + 1000
        new_plan((p, new_d), costs[p, d] + 1000, pathss[p, d])

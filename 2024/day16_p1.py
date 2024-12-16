from common import *
from collections import defaultdict
import heapq
a = get_input().grid

start = a.extract("S", ".")
end = a.extract("E", ".")

costs = defaultdict(lambda: float("inf"))
q = []

def new_plan(state, cost):
    if cost < costs[state]:
        costs[state] = cost
        heapq.heappush(q, (cost, state))

new_plan((start, (1, 0)), 0)

while q:
    _, (p, d) = heapq.heappop(q)

    if p == end:
        print(_)
        exit(0)

    # step forward
    new_p = offset(p, d)
    if a[new_p] == ".":
        new_plan((new_p, d), costs[(p, d)] + 1)

    # turn
    for new_d in [(-d[1], d[0]), (d[1], -d[0])]:
        new_cost = costs[(p, d)] + 1000
        new_plan((p, new_d), costs[(p, d)] + 1000)

from common import *
from collections import defaultdict
import heapq
a = get_input()

WIDTH, HEIGHT = 71, 71

g = Grid(WIDTH, HEIGHT, ".")

def do_pathfinding():
    start = 0, 0
    end = WIDTH-1, HEIGHT-1

    costs = defaultdict(lambda: float("inf"))
    q = []
    
    def new_plan(state, cost):
        if cost < costs[state]:
            costs[state] = cost
            heapq.heappush(q, (cost, state))
    
    new_plan(start, 0)
    
    while q:
        _, p = heapq.heappop(q)
    
        if p == end:
            return _
    
        # moves
        for new_p in g.orthogonals(p):
            if g[new_p] == ".":
                new_plan(new_p, costs[p] + 1)

from tqdm import tqdm
for x, y in tqdm(a):
    g[x, y] = "#"
    if not do_pathfinding():
        print(x, y)
        break

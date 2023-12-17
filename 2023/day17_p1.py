from common import *
import queue
from dataclasses import dataclass
a = get_input().grid.map(int)
goal = a.width-1, a.height-1

@dataclass(frozen=True, order=True)
class Node:
    pos: tuple[int, int]
    d: tuple[int, int]
    count: int

def heuristic(a):
    a = a.pos
    return abs(a[0]-goal[0])+abs(a[1]-goal[1])

start = Node((0, 0), (1, 0), 0)
frontier: queue.PriorityQueue[tuple[int, Node]] = queue.PriorityQueue()
frontier.put((heuristic(start), start))
fromstart = {start: 0}
crumbs = {}

while frontier:
    cost, current = frontier.get()
    if current.pos == goal:
        print(fromstart[current])
        exit(0)

    p = current.pos
    dx, dy = current.d

    moves = []

    # turn left
    nd = -dy, dx
    np = offset(p, nd)
    if np in a:
        moves.append(Node(np, nd, 0))

    # turn right
    nd = dy, -dx
    np = offset(p, nd)
    if np in a:
        moves.append(Node(np, nd, 0))

    # go straight
    np = offset(current.pos, current.d)
    if np in a and current.count < 2:
        new_count = current.count + 1 if current.pos != (0, 0) else 0
        moves.append(Node(np, current.d, new_count))

    for move in moves:
        tg = fromstart[current] + a[move.pos]
        if tg < fromstart.get(move, float('inf')):
            fromstart[move] = tg
            crumbs[move] = current
            frontier.put((tg + heuristic(move), move))

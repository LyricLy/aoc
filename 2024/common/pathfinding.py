import heapq
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable, Iterator, Callable

__all__ = ("pathfind",)

@dataclass(order=True)
class Priority[S]:
    state: S = field(compare=False)
    priority: float

def trace_paths(origins, to):
    our_origins = origins.get(to)
    if not our_origins:
        yield [to]
        return
    for origin in our_origins:
        for path in trace_paths(origins, origin):
            yield path + [to]

def pathfind[S](start: S, end: Callable[[S], bool], step: Callable[[S], Iterable[tuple[S, int]]], heuristic: Callable[[S], float] = lambda _: 0) -> Iterator[list[S]]:
    origins = {}
    cost_to = defaultdict(lambda: float("inf"), {start: 0})
    frontier = [Priority(start, 0)]

    while frontier:
        p = heapq.heappop(frontier).state

        if end(p):
            return trace_paths(origins, p)

        for adj, cost in step(p):
            g = cost_to[p] + cost
            if g < cost_to[adj]:
                cost_to[adj] = g
                origins[adj] = [p]
                heapq.heappush(frontier, Priority(adj, g + heuristic(adj)))
            elif g == cost_to[adj]:
                origins[adj].append(p)

    return iter(())

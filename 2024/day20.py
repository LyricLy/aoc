from common import *
from collections import deque
import itertools
a = get_input().grid
start = a.extract("S", ".")
end = a.extract("E", ".")

frontier = deque([(end, 0)])

while frontier:
    p, c = frontier.popleft()
    if a[p] != ".":
        continue
    a[p] = c
    for x in Grid.orthogonals(p):
        frontier.append((x, c+1))

c = 0
for starter, ender in itertools.combinations([p for p in a if a[p] != "#"], 2):
    dist = abs(starter[0]-ender[0])+abs(starter[1]-ender[1])
    if dist <= 20:
        if abs(a[starter] - a[ender]) - dist >= 100:
            c += 1
print(c) 

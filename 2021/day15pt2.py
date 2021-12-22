from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

with open("input.txt") as f:
    t = f.read()
import common
g = common.Grid.parse(t, int)
ng = common.Grid(g.width*5, g.height*5, g.data*25)
def succ(r, n):
    for _ in range(n):
        r += 1
        if r == 10:
            r = 1
    return r
for x, y in g:
    ng[x, y] = g[x, y]
    for dy in range(5):
        for dx in range(5):
            ng[x+g.width*dx, y+g.height*dy] = succ(g[x, y], dx+dy)

print(ng)

grid = Grid(matrix=[ng.take(r) for r in ng.rows()])
start = grid.node(0, 0)
end = grid.node(ng.width-1, ng.height-1)
finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)
print(sum(ng[t] for t in path[1:]))

import itertools
from common import Grid, offset

example = 0
with open("example.txt" if example else "input.txt") as f:
    t = f.read().strip()

rocks = [Grid.parse(x, lambda x: x) for x in """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split("\n\n")]

grid = Grid(7, 10000, ".")
top = 9999

def true_rock_loc(rock, rp, p):
    return (p[0]+rp[0], rp[1]-(rock.height-p[1]-1))

buffets = itertools.cycle(t)
top_changes = ""

for _, rock in zip(range(4000), itertools.cycle(rocks)):
    rock_pos = 2, top-3
    for buffet in buffets:
        buffet_dir = (1, 0) if buffet == ">" else (-1, 0)
        for p in rock:
            if rock[p] != "#":
                continue
            if grid[offset(true_rock_loc(rock, rock_pos, p), buffet_dir)] in ("#", None):
                break
        else:
            rock_pos = offset(rock_pos, buffet_dir)

        for p in rock:
            if rock[p] != "#":
                continue
            if grid[offset(true_rock_loc(rock, rock_pos, p), (0, 1))] in ("#", None):
                break
        else:
            rock_pos = offset(rock_pos, (0, 1))
            continue

        break
    for p in rock:
        if rock[p] != "#":
            continue
        grid[true_rock_loc(rock, rock_pos, p)] = "#"
    new_top = min(top, rock_pos[1]-rock.height)
    top_changes += str(top-new_top)
    top = new_top

print(top_changes)

with open("input.txt") as f:
    elves = [[int(y) for y in x.splitlines()] for x in f.read().split("\n\n")]

import itertools
print(sum(itertools.chain.from_iterable(list(sorted(elves, key=sum))[-3:])))

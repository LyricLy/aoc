import itertools


with open("input.txt") as f:
    inp = [*map(int, f.readlines())]


for x, y in itertools.combinations(range(len(inp)), 2):
    if sum(inp[x:y+1]) == 258585477:
        t = inp[x:y+1]
        print(min(t) + max(t))
        break

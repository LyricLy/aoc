from collections import defaultdict

with open("input.txt") as f:
    t = f.read()

rolls = [3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 6, 5, 6, 7, 6, 7, 8, 5, 6, 7, 6, 7, 8, 7, 8, 9]
print(sorted(rolls))

universe = defaultdict(int, {(int(t.splitlines()[0].split()[-1]), int(t.splitlines()[1].split()[-1]), 0, 0): 1})
winners = [0, 0]

while universe:
    for key in list(universe):
        v = universe.pop(key)
        p1, p2, p1s, p2s = key
        for roll in rolls:
            p1c = (p1+roll-1)%10+1
            p1sc = p1s+p1c
            if p1sc >= 21:
                winners[0] += v
                continue
            for roll in rolls:
                p2c = (p2+roll-1)%10+1
                p2sc = p2s+p2c
                if p2sc >= 21:
                    winners[1] += v
                    continue
                universe[(p1c, p2c, p1sc, p2sc)] += v

print(max(winners))

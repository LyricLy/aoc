with open("input.txt") as f:
    t = f.read().removesuffix("\n")

inp = [tuple(map(lambda x: tuple(map(int, x.split("-"))), x.split(","))) for x in t.splitlines()]

c = 0
for x, y in inp:
    if x[1] >= y[0] and x[0] <= y[0] or y[1] >= x[0] and y[0] <= x[0]:
        c += 1
print(c)

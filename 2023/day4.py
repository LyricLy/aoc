with open("input.txt") as f:
    r = f.read().split("\n")[:-1]

mul = [1 for _ in range(len(r))]

for idx, card in enumerate(r):
    a, b = card.split(": ")
    c, d = b.split(" | ")
    winning = [int(x) for x in c.split()]
    gaming = [int(x) for x in d.split()]
    bb = sum(x in winning for x in gaming)
    for i in range(idx+1, idx+1+bb):
        mul[i] += mul[idx]

print(sum(mul))

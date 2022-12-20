example = 0

with open("example.txt" if example else "input.txt") as f:
    t = f.read()

data = [int(x)*811589153 for x in t.splitlines()]
indices = list(range(len(data)))

for _ in range(10):
    for ix in range(len(data)):
        i = indices.index(ix)
        num = data[i]
        nn, n = divmod(i + num, len(data))
        while nn:
            nn, n = divmod(n + nn, len(data))
        data.pop(i)
        data.insert(n, num)
        indices.pop(i)
        indices.insert(n, ix)

i = data.index(0)
s = 0
for di in (1000, 2000, 3000):
    s += data[(i+di) % len(data)]
print(s)

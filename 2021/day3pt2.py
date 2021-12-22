with open("input.txt") as f:
    i = f.read().splitlines()

import statistics

b = 0
while True:
    g = [max(statistics.multimode("".join(x))) for x in zip(*i)]
    e = [min(statistics.multimode("".join("1" if k == "0" else "0" for k in x))) for x in zip(*i)]
    i = [x for x in i if x[b] == g[b]]
    if len(i) == 1:
        j = int(i[0], 2)
        break
    b += 1

with open("input.txt") as f:
    i = f.read().splitlines()

b = 0
while True:
    g = [max(statistics.multimode("".join(x))) for x in zip(*i)]
    e = [min(statistics.multimode("".join("1" if k == "0" else "0" for k in x))) for x in zip(*i)]
    i = [x for x in i if x[b] == e[b]]
    if len(i) == 1:
        k = int(i[0], 2)
        break
    b += 1

print(j)
print(k)

print (j * k)

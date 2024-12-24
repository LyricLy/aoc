from common import *
import random
a = get_input()

# swaps:
# nbc with svm
# z15 with kqk
# z23 with cgq
# z39 with fnr

known = {}
start = (1 << 45) - 1
x_in = random.randint(0, start)
y_in = random.randint(0, start)
highest_set = -1
for n in range(45):
    x_has = bool((1 << n) & x_in)
    y_has = bool((1 << n) & y_in)
    if x_has or y_has:
        highest_set = n
    known[f"x{n:02}"] = x_has
    known[f"y{n:02}"] = y_has

gates = {
    "AND": lambda x, y: x and y,
    "OR": lambda x, y: x or y,
    "XOR": lambda x, y: x != y,
}

while True:
    for x, gate, y, out in a[1].dechaff:
        if x in known and y in known and out not in known:
            known[out] = gates[gate](known[x], known[y])
            break
    else:
        break

print(known)

c = 0
for i in range(0, 100):
    k = f"z{i:02}"
    if k not in known:
        break
    c += (1 << i) * known[k]
print(highest_set, f"\n  {x_in:045b}\n+ {y_in:045b}\n= {x_in + y_in:045b}\n≠ {c:045b}\n{x_in + y_in} vs {c}")
if c != x_in + y_in:
    print("WRONG!!!")

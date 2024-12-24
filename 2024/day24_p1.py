from common import *
a = get_input()

known = {x: y.num == 1 for x, y in a[0].header_map.items()}

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

c = 0
for i in range(0, 100):
    k = f"z{i:02}"
    if k not in known:
        break
    c += (1 << i) * known[k]
print(c)

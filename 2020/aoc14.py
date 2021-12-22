from aoccy import *
from collections import defaultdict

@ lit("mask = ") >> (lit("0") | lit("1") | lit("X"))[:] << lit("\n")
def mask_set(l):
    return (1, l)

@ lit("mem[") >> (regex("\d+") << lit("] = ")) & regex("\d+") << lit("\n")
def mem_set(l):
    return (0, int(l[0].group(0)), int(l[1].group(0)))

program = (mask_set | mem_set)[:]


with open("input.txt") as f:
    data = program.parse_text(f.read())

mask = None
mem = defaultdict(int)
for t, *d in data:
    if t == 1:
        mask = d[0]
    elif t == 0:
        addr = bin(d[0])[2:].zfill(36)
        addrs = []
        iis = []
        for i, c in enumerate(mask):
            if c == "X":
                iis.append(i)
        for n in range(2**len(iis)):
            new_addr = list(addr)
            for i, z in zip(iis, bin(n)[2:].zfill(len(iis))):
                new_addr[i] = z
            addrs.append(new_addr)
        for i, c in enumerate(mask):
            if c == "1":
                for a in addrs:
                    a[i] = "1"
        for addr in addrs:
            mem[int("".join(addr), 2)] = d[1]

print(sum(mem.values()))

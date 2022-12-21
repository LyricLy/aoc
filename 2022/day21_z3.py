import z3
from graphlib import TopologicalSorter

example = 0

with open("example.txt" if example else "input.txt") as f:
    t = f.read()

monkeys = {x: y for line in t.splitlines() for x, y in [line.split(": ")]}

prereqs = {x: y.split()[::2] if not y.isdigit() else [] for x, y in monkeys.items()}

d = {}
s = z3.Solver()
for m in TopologicalSorter(prereqs).static_order():
    if m == "root":
        x, _, y = monkeys[m].split()
        e = f"{x} == {y}"
    elif m == "humn":
        e = "True"
    else:
        e = f"{m} == {monkeys[m]}"
    exec(f"{m} = z3.Int(m); s.add({e})", globals(), d)

s.check()
print(s.model()[d["humn"]])

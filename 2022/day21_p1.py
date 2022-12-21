from graphlib import TopologicalSorter

example = 0

with open("example.txt" if example else "input.txt") as f:
    t = f.read()

monkeys = {x: y for line in t.splitlines() for x, y in [line.split(": ")]}

prereqs = {x: y.split()[::2] if not y.isdigit() else [] for x, y in monkeys.items()}

d = {}
for m in TopologicalSorter(prereqs).static_order():
    exec(f"{m} = {monkeys[m]}", {}, d)
print(d["root"])

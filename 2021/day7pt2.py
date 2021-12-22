with open("input.txt") as f:
    t = f.read()

ns = [int(x) for x in t.split(",")]

print(min(sum(abs(x-y)*(abs(x-y)+1)//2 for y in ns) for x in range(0, max(ns)+1)))

with open("input.txt") as f:
    i = f.read()

n = [int(x) for x in i.split()]
prev = None
c = 0
for j in range(len(n)):
    b = sum(n[j:j+3])
    if prev is not None and b > prev:
        c += 1
    prev = b
print(c)

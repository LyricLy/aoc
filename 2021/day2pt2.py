with open("input.txt") as f:
    i = f.read()

depth = 0
horiz = 0
aim = 0
for inst in i.splitlines():
    c, n = inst.split()
    n = int(n)
    match c:
        case "forward":
            horiz += n
            depth += aim * n
        case "down":
            aim += n
        case "up":
            aim -= n
print(horiz*depth)

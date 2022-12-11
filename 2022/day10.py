import common

exmaple = open("inputs/2022-10").read()

def go(t):
    x = 1
    cycles = []
    s = 0
    for inst in t.splitlines():
        match inst.split():
            case ["addx", n]:
                cycles.append("noop")
                cycles.append(("add", int(n)))
            case ["noop"]:
                cycles.append("noop")
    crt = common.Grid(40, 6, ".")
    for i, cycle in enumerate(cycles):
        j = i % 40
        crt.data[i] = "#" if x == j or x == j-1 or x == j+1 else "."
        match cycle:
            case ["add", n]:
                x += n
        print(i)
    print(crt)

print(go(exmaple))

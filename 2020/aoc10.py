with open("input.txt") as f:
    data = list(map(int, f.readlines()))

def do_jolts(jolts):
    jolts.append(max(jolts) + 3)
    jolts.append(0)
    jolts.sort()
    t = [0]*len(jolts)
    t[0] = 1
    for i, jolt in enumerate(jolts[:-1]):
        print(jolt, t[i])
        possible = [ix for ix, x in enumerate(jolts[i+1:i+4], start=i+1) if x - jolt <= 3]
        for ix in possible:
            t[ix] += t[i]
    return t[-1]

print(do_jolts(data))

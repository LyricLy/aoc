with open("input.txt") as f:
    data = [list(x.strip()) for x in f.readlines()]

def loc_at(x, y):
    if x < 0 or y < 0:
        return "."
    try:
        return data[y][x]
    except IndexError:
        return "."

def hash_state():
    return tuple(tuple(x) for x in data)

def print_thing():
    print("\n".join(" ".join(t) for t in data))
    print("\n===\n")

def do_step():
    now = hash_state()
    places = []
    for y, t in enumerate(data):
        places.append([])
        for x, v in enumerate(t):
            places[-1].append(sum(loc_at(x + dx, y + dy) == "#" for dx in range(-1, 2) for dy in range(-1, 2) if dx or dy))
    for y, t in enumerate(data):
        for x, v in enumerate(t):
            if v == ".": pass
            elif v == "L" and places[y][x] == 0:
                data[y][x] = "#"
            elif v == "#" and places[y][x] >= 4:
                data[y][x] = "L"
    return hash_state() != now

while do_step(): pass
count = 0
for t in data:
    for v in t:
        if v == "#":
            count += 1
print(count)

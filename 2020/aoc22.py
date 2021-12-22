with open("input.txt") as f:
    data = f.read().split("\n\n")
    p1 = [*map(int, data[0].splitlines()[1:])]
    p2 = [*map(int, data[1].splitlines()[1:])]

def game(p1, p2):
    prev = set()
    while p1 and p2:
        state = tuple(p1), tuple(p2)
        if state in prev:
            return False
        prev.add(state)
        x = p1.pop(0)
        y = p2.pop(0)
        if x <= len(p1) and y <= len(p2):
            winner = game(p1[:x], p2[:y])
        else:
            winner = y > x
        if not winner:
            p1.extend((x, y))
        else:
            p2.extend((y, x))
    return False if p1 else True

print(len(p2), len(p1))

winner = p2 if game(p1, p2) else p1
print(sum(x * y for x, y in zip(reversed(winner), range(1, len(winner)+1))))

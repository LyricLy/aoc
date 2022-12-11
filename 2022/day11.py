with open("example.txt") as f:
    t = f.read().rstrip()

monkeys = []
for monkey in t.split("\n\n"):
    lines = monkey.splitlines()
    class Monkey:
        items = [int(x) for x in lines[1].split(": ")[1].split(", ")]
        operator = lines[2].split(" = ")[1]
        test = int(lines[3].split(" by ")[1])
        true_target = int(lines[4].split(" ")[-1])
        count = 0
        false_target = int(lines[5].split(" ")[-1])
    monkeys.append(Monkey)

import math
max_test = math.lcm(*[monkey.test for monkey in monkeys])

for _ in range(10_000):
    for monkey in monkeys:
        for item in monkey.items:
            new = eval(monkey.operator, {"old": item}) % max_test
            monkeys[monkey.true_target if new % monkey.test == 0 else monkey.false_target].items.append(new)
            monkey.count += 1
        monkey.items.clear()
l = [monkey.count for monkey in monkeys]
a, b = sorted([monkey.count for monkey in monkeys])[-2:]

def priority(s):
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(s) + 1
with open("input.txt") as f:
    sacks = f.read().splitlines()

# s = 0
# for sack in sacks:
    # first, second = sack[:len(sack)//2], sack[len(sack)//2:]
    # c = (set(first) & set(second)).pop()
    # s += priority(c)
# print(s)

s = 0
for group in [sacks[i:i+3] for i in range(0, len(sacks), 3)]:
    c = set.intersection(*map(set, group)).pop()
    s += priority(c)
print(s)

from common import *
a = Aoc(get_input().string.replace("\n",""))

def h(s):
    current = 0
    for c in s:
        current += ord(c)
        current *= 17
        current %= 256
    return current

print(sum(h(x.string) for x in a.split(",")))

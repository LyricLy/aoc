with open("input.txt") as f:
    r = f.read()

def to_digit(a):
    return str({"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}.get(a, a))

def search_in_reverse(r):
    return [x[::-1] for x in re.findall(r"one|two|three|four|five|six|seven|eight|nine"[::-1] + r"|\d", r[::-1])]

import re
t = [int(to_digit(re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", l)[0]) + to_digit(search_in_reverse(l)[0])) if True else None for l in r.split("\n") if l]
print(sum(t))

from common import *
a = get_input()
import re
t=str(a)
c = 0
do = True
for b in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", t):
    if b[0] == "do()":
        do = True
    elif b[0] == "don't()":
        do = False
    elif do:
        c += int(b[1])*int(b[2])
print(c)

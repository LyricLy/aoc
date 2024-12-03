from common import *
a = get_input()
import re
t=str(a)
c = 0
for b in re.finditer(r"mul\((\d+),(\d+)\)", t):
    c += int(b[1])*int(b[2])
print(c)

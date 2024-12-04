from common import *
a = get_input().grid

c = 0
for p in a:
    for d in directions:
        np = p
        for letter in "XMAS":
            if a[np] != letter:
                break
            np = offset(np, d)
        else:
            c += 1
print(c)

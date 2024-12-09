from common import *
import math
a = [int(x) if i % 2 else (i // 2, int(x)) for i, x in enumerate(list(get_input().string))]

def print_a():
    for i in range(0, len(a), 2):
        id, length = a[i]
        print(str(id)+"-"*(length-len(str(id))), end="")
        if i+1 < len(a):
            print("."*a[i+1], end="")
    print()

for target_e in range(len(a) // 2 + 1)[::-1]:
    target = [i*2 for i, (id, _) in enumerate(a[::2]) if id == target_e][0]
    id, length = a[target]
    for idx, space in enumerate(a[1:target:2]):
        if space >= length:
            a[target-1:target+2] = [length + a[target-1] + a[target+1]] if target != len(a)-1 else []
            a[idx*2+1:idx*2+2] = [0, (id, length), a[idx*2+1] - length]
            break

pos = 0
c = 0
for i, (id, length) in enumerate(a[::2]):
    c += (math.comb(pos+length, 2)-math.comb(pos, 2)) * id
    pos += sum(a[i*2+1:i*2+2]) + length
print(c)

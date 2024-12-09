from common import *
a = [int(x) for x in list(get_input().string)] + [0]

area = []

for i, (x, y) in enumerate(zip(*[iter(a)]*2)):
    area.extend([i]*x)
    area.extend([None]*y)

while True:
    if (val := area.pop()) is None:
        continue
    for j in range(len(area)):
        if area[j] is None:
            area[j] = val
            break
    else:
        break
area.append(val)

print(area)
print(sum([i * x for i, x in enumerate(area)]))



from common import *
a = [int(x) for x in str(get_input()).split()]

for _ in range(25):
    a = sum([[1] if not stone else [stone*2024] if len(str(stone)) % 2 else [int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])] for stone in a], start=[])
    print(len(a))

print(len(a))

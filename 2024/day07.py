from common import *
a = get_input()

def can_do_it(target, nums):
    assert len(nums) > 1
    frontier = {nums[0]}
    for num in nums[1:]:
        frontier = {x + num for x in frontier} | {x * num for x in frontier} | {int(f"{x}{num}") for x in frontier}
    return target in frontier

from tqdm import tqdm
c = 0
for b in tqdm(a):
    if can_do_it(b.id, b.nums):
        c += b.id
print(c)

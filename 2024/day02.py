from common import *
import itertools
a = get_input()

c = 0
for report in a:
    valid = all(1 <= y - x <= 3 for x, y in itertools.pairwise(report.nums)) or all(1 <= y - x <= 3 for x, y in itertools.pairwise(report.nums[::-1])) or any(
        [all(1 <= y - x <= 3 for x, y in itertools.pairwise(report.nums[:i] + report.nums[i+1:])) or all(1 <= y - x <= 3 for x, y in itertools.pairwise((report.nums[:i] + report.nums[i+1:])[::-1])) for i in range(len(report.nums))]
    )
    c += valid
print(c)

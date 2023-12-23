from __future__ import annotations

import bisect
import random
import math
from typing import Iterator, Iterable, Self


class UnsignedRangeSet:
    __slots__ = ("ranges",)

    ranges: list[tuple[int, int]]

    def __init__(self, ns: Iterable[int] = ()):
        self.ranges = []
        self.update(ns)

    @classmethod
    def from_ranges(cls, ranges: list[tuple[int, int]]) -> Self:
        rs = cls.__new__(cls)
        rs.ranges = ranges
        return rs

    def _bisect(self, x: int, *, upper_bound: bool = False):
        return bisect.bisect(self.ranges, x, key=lambda x: x[not upper_bound])

    def __repr__(self):
        return f"UnsignedRangeSet({self.ranges})"

    def __str__(self):
        return f"{{{', '.join(f'{start}..{stop}' for start, stop in self.ranges)}}}"

    def _add_range(self, start: int, stop: int):
        if stop <= start:
            return
        i = self._bisect(start-1)
        j = self._bisect(stop, upper_bound=True)
        old = self.ranges[i:j]
        if old:
            start = min(start, old[0][0])
            stop = max(stop, old[-1][1])
        self.ranges[i:j] = [(start, stop)] 

    def add(self, n: int):
        self._add_range(n, n+1)

    def update(self, *nss: Iterable[int]):
        for ns in nss:
            if isinstance(ns, range) and ns.step == 1:
                self._add_range(ns.start, ns.stop)
            else:
                for n in ns:
                    self.add(n)

    def __contains__(self, item: int):
        i = self._bisect(item)
        if i >= len(self.ranges):
            return False
        start, stop = self.ranges[i]
        return start <= item < stop

    def __iter__(self) -> Iterator[int]:
        for x, y in self.ranges:
            yield from range(x, y)

    def __len__(self):
        return sum(y - x for x, y in self.ranges)

    def __getitem__(self, i: int) -> int:
        for x, y in self.ranges:
            l = y - x
            if i < l:
                return x + i
            i -= l
        raise IndexError("index out of range")

    def copy(self) -> Self:
        return self.from_ranges(self.ranges.copy())

    def affine_transform(self, times: int = 1, plus: int = 0) -> Self:
        return self.from_ranges([(x*times+plus, y*times+plus) for x, y in self.ranges])

    def sum(self) -> int:
        return sum((y-x) * (x+y-1) // 2 for x, y in self.ranges)

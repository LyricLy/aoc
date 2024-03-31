"""A set backed by a list of ranges that stores contiguous integers efficiently.

This module exports a single type `rangeset` that matches the interface of `set` with the following changes and additions:
- Only `int`s can be stored in the set. Otherwise, things go very wrong very quickly.
- The `rangeset` constructor, as well as any method that accepts an `Iterable[int]`, special-cases `range` objects, giving performance that is constant time in the size of the range. 
- `rangeset` does not subclass `set` or `collections.abc.Set`
    - I couldn't be bothered to make the types for this line up and it's not that relevant to aoc
- `rangeset.from_ranges` builds a range set from a list of ranges represented as 2-tuples. The ranges passed must be non-overlapping, non-empty, and sorted from lowest to highest. This condition is not checked.
- The comparison operators `>`, `<`, `<=`, `>=` work only with other `rangeset`s, not all `Set`s
    - `issubset`, `issuperset`, and `isdisjoint` still work with iterables like usual
- The type is hashable, despite being mutable. Be careful!
    - `__eq__` and `__hash__` are not compatible with other `Set`s
- Empty `rangeset`s identify themselves as `rangeset()` instead of `set()` in `__repr__`, and ranges are collapsed in the representation: `{1, 2, 3}` is shown as `{1..3}`.
- `__getitem__` can be used to access the values in sorted order. For example `s[0]` accesses the smallest int in the set and `s[-1]` the largest. Note that slicing is not currently supported.
- `rangeset.union()` and `rangeset.symmetric_difference()` can be used without arguments, returning empty rangesets.
- `rangeset.symmetric_difference` can be used with other numbers of arguments than 2.
- `rangeset.discard` now returns a bool indicating whether or not the element was found in the set before discarding.
- Set operators such as `|` and `&` work with any `Iterable[int]`, not just other `rangeset`s
- `rangeset.affine_transform` is provided to apply an affine transformation on the endpoints of each range
    - Note that this is slightly different to mapping: `[x*2 for x in rangeset(range(5))]` is `[0, 2, 4, 6, 8]`, while `list(rangeset(range(5)).affine_transform(times=2))` is `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- `rangeset.sum` is a more efficient way to sum a range set than `sum()`, using the well-known closed form for the sum of an integer range
"""

from __future__ import annotations

import bisect
from typing import Iterator, Iterable


__all__ = ("rangeset", "irange")


def _to_ranges(nss: tuple[Iterable[int], ...]) -> Iterator[list[tuple[int, int]]]:
    for ns in nss:
        if isinstance(ns, range) and ns.start < ns.stop and ns.step == 1:
            yield [(ns.start, ns.stop)]
        elif isinstance(ns, rangeset):
            yield ns.ranges
        else:
            l: list[tuple[int, int]] = []
            for n in sorted(ns):
                if not l or n > l[-1][1]:
                    l.append((n, n+1))
                else:
                    l[-1] = l[-1][0], n+1
            yield l

def irange(left, right):
    if left <= right:
        return range(left, right+1)
    else:
        return range(left, right-1, -1)


class rangeset:
    __slots__ = ("ranges",)

    ranges: list[tuple[int, int]]

    def __init__(self, ns: Iterable[int] = ()):
        self.ranges = []
        self.update(ns)

    @classmethod
    def from_ranges(cls, ranges: list[tuple[int, int]]) -> rangeset:
        rs = cls.__new__(cls)
        rs.ranges = ranges
        return rs

    # for debugging; never called in normal operation
    def _sanity_check(self):
        import itertools
        for (a, b), (c, d) in itertools.pairwise(self.ranges):
            assert a < b < c < d

    def _bisect(self, x: int, *, upper_bound: bool = False):
        l = len(self.ranges)
        if l < 16:
            # don't bisect
            for i, r in enumerate(self.ranges):
                if x < r[not upper_bound]:
                    return i
            return l
        return bisect.bisect(self.ranges, x, key=lambda x: x[not upper_bound])

    def _range_bounds(self, start: int, stop: int) -> tuple[int, int]:
        return self._bisect(start), self._bisect(stop-1, upper_bound=True)

    def _compare(self, other: rangeset, *, no_eq: bool = False):
        i = 0
        j = 0
        while i < len(self.ranges) and j < len(other.ranges):
            a = self.ranges[i]
            b = other.ranges[j]
            if a == b:
                i += 1
                j += 1
                continue

            if a[0] < b[0]:
                return False
            if a[1] > b[1]:
                j += 1
            else:
                i += 1

        return j < len(other.ranges) if no_eq else i >= len(self.ranges)

    def __eq__(self, other: object):
        if not isinstance(other, rangeset):
            return NotImplemented
        return self.ranges == other.ranges

    def __ne__(self, other: object):
        if not isinstance(other, rangeset):
            return NotImplemented
        return self.ranges != other.ranges

    def __le__(self, other: rangeset):
        return self._compare(other)

    def issubset(self, other: Iterable[int]) -> bool:
        if not isinstance(other, rangeset):
            other = rangeset(other)
        return self <= other

    def __ge__(self, other: rangeset):
        return other._compare(self)

    def issuperset(self, other: Iterable[int]) -> bool:
        if not isinstance(other, rangeset):
            other = rangeset(other)
        return self >= other

    def __lt__(self, other: rangeset):
        return self._compare(other, no_eq=True)

    def __gt__(self, other: rangeset):
        return self._compare(other, no_eq=True)

    def isdisjoint(self, other: Iterable[int]) -> bool:
        if not isinstance(other, rangeset):
            # dumb ver
            return all(x not in self for x in other)

        i = 0
        j = 0
        while i < len(self.ranges) and j < len(other.ranges):
            a = self.ranges[i]
            b = other.ranges[j]
            if a[1] <= b[0]:
                i += 1
            elif b[1] <= a[0]:
                j += 1
            else:
                return False

        return True

    def __hash__(self):
        return hash(tuple(self.ranges))

    def __repr__(self):
        if not self:
            return "rangeset()"
        return f"{{{', '.join(f'{start}..{stop-1}' for start, stop in self.ranges)}}}"

    def __bool__(self):
        return bool(self.ranges)

    def __contains__(self, item: int):
        i = self._bisect(item)
        if i >= len(self.ranges):
            return False
        start, stop = self.ranges[i]
        return start <= item < stop

    def __iter__(self) -> Iterator[int]:
        for x, y in self.ranges:
            yield from range(x, y)

    def __reversed__(self) -> Iterator[int]:
        for x, y in reversed(self.ranges):
            yield from range(y-1, x-1, -1)

    def __len__(self):
        return sum(y - x for x, y in self.ranges)

    def __getitem__(self, i: int) -> int:
        if i < 0:
            i = ~i
            for x, y in reversed(self.ranges):
                l = y - x
                if i < l:
                    return y - 1 - i
                i -= l
        else:
            for x, y in self.ranges:
                l = y - x
                if i < l:
                    return x + i
                i -= l

        raise IndexError("index out of range")

    def _add_range(self, start: int, stop: int):
        # happy cases
        if not self.ranges:
            self.ranges.append((start, stop))
            return

        last_start, last_stop = self.ranges[-1]
        if start >= last_start:
            if start <= last_stop:
                if stop > last_stop:
                    self.ranges[-1] = last_start, stop
            else:
                self.ranges.append((start, stop))
            return

        first_start, first_stop = self.ranges[0]
        if stop <= first_stop:
            if stop >= first_start:
                if start < first_start:
                    self.ranges[0] = start, first_stop
            else:
                self.ranges.insert(0, (start, stop))
            return

        i, j = self._range_bounds(start-1, stop+1)
        if i != j:
            start = min(start, self.ranges[i][0])
            stop = max(stop, self.ranges[j-1][1])
        self.ranges[i:j] = [(start, stop)]

    def add(self, n: int):
        self._add_range(n, n+1)

    def update(self, *nss: Iterable[int]):
        for rs in _to_ranges(nss):
            it = iter(rs)
            for r in it:
                if not self or r[0] > self.ranges[-1][1]:
                    self.ranges.append(r)
                    self.ranges.extend(it)
                    break
                self._add_range(*r)

    def union(*others: Iterable[int]) -> rangeset:
        rs = rangeset()
        rs.update(*others)
        return rs

    def _discard_range(self, start: int, stop: int) -> bool:
        i, j = self._range_bounds(start, stop)
        if i == j:
            return False

        rs: list[tuple[int, int]] = []
        if start in range(*self.ranges[i])[1:]:
            rs.append((self.ranges[i][0], min(self.ranges[i][1], start)))
        if stop in range(*self.ranges[j-1])[:-1]:
            rs.append((max(self.ranges[j-1][0], stop), self.ranges[j-1][1]))

        self.ranges[i:j] = rs
        return True

    def discard(self, n: int) -> bool:
        return self._discard_range(n, n+1)

    # I hate this function but it's included for set compat
    def remove(self, n: int):
        if not self.discard(n):
            raise KeyError(n)

    def difference_update(self, *nss: Iterable[int]):
        for rs in _to_ranges(nss):
            for r in rs:
                self._discard_range(*r)

    def difference(self, *others: Iterable[int]) -> rangeset:
        rs = self.copy()
        rs.difference_update(*others)
        return rs

    def _in_range(self, start: int, stop: int) -> rangeset:
        i, j = self._range_bounds(start, stop)

        rs = self.ranges[i:j]
        if rs:
            rs[0] = max(rs[0][0], start), rs[0][1]
            rs[-1] = rs[-1][0], min(rs[-1][1], stop)

        return self.from_ranges(rs)

    def intersection_update(self, *nss: Iterable[int]):
        # this is a "fake" update (not in-place), which is consistent with CPython's implementation of set.intersection_update
        if not nss:
            return
        self.ranges = self.intersection(*nss).ranges

    def intersection(self, *others: Iterable[int]) -> rangeset:
        if not others:
            return self.copy()

        current = self
        for rs in _to_ranges(others):
            new = rangeset()
            for r in rs:
                new.update(current._in_range(*r))
            current = new

        return current

    def _xor_range(self, start: int, stop: int):
        i, j = self._range_bounds(start, stop)
        if i == j:
            self._add_range(start, stop)
            return

        rs: list[tuple[int, int]] = []
        def add_range_to_rs(start: int, stop: int):
            if stop-start >= 1:
                rs.append((start, stop))

        start, poststart = sorted((start, self.ranges[i][0]))
        if poststart-start >= 1:
            add_range_to_rs(start, poststart)

        puck = self.ranges[i][1]
        for r in self.ranges[i+1:j-1]:
            add_range_to_rs(puck, r[0])
            puck = r[1]

        prestop, stop = sorted((stop, self.ranges[j-1][1]))
        add_range_to_rs(puck, self.ranges[j-1][0])
        if stop-prestop >= 1:
            add_range_to_rs(prestop, stop)

        self.ranges[i:j] = rs

    def symmetric_difference_update(self, *nss: Iterable[int]):
        for rs in _to_ranges(nss):
            it = iter(rs)
            for r in it:
                if not self or r[0] > self.ranges[-1][1]:
                    self.ranges.append(r)
                    self.ranges.extend(it)
                    break
                self._xor_range(*r)

    def symmetric_difference(*others: Iterable[int]) -> rangeset:
        rs = rangeset()
        rs.symmetric_difference_update(*others)
        return rs

    def __or__(self, other: Iterable[int]) -> rangeset:
        return self.union(other)

    def __ior__(self, other: Iterable[int]):
        self.update(other)
        return self

    def __and__(self, other: Iterable[int]) -> rangeset:
        return self.intersection(other)

    def __iand__(self, other: Iterable[int]):
        self.intersection_update(other)
        return self

    def __sub__(self, other: Iterable[int]):
        return self.difference(other)

    def __isub__(self, other: Iterable[int]):
        self.difference_update(other)
        return self

    def __xor__(self, other: Iterable[int]):
        return self.symmetric_difference(other)

    def __ixor__(self, other: Iterable[int]):
        self.symmetric_difference(other)
        return self

    def copy(self) -> rangeset:
        return self.from_ranges(self.ranges.copy())

    def affine_transform(self, times: int = 1, plus: int = 0) -> rangeset:
        return self.from_ranges([(x*times+plus, y*times+plus) for x, y in self.ranges])

    def sum(self) -> int:
        return sum((y-x) * (x+y-1) // 2 for x, y in self.ranges)

    def pop(self) -> int:
        if not self:
            raise KeyError("pop from an empty rangeset")
        r = self.ranges[-1]
        if r[1]-r[0] == 1:
            self.ranges.pop()
        else:
            self.ranges[-1] = r[0], r[1]-1
        return r[1]-1

    def clear(self):
        self.ranges.clear()

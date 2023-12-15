from __future__ import annotations

import itertools
import functools
from typing import TypeVar, Callable, Any, Generic, Optional, Iterable, Iterator


T = TypeVar("T")
G = TypeVar("G")
P = ParamSpec('P')
Dir = tuple[int, int]
Point = tuple[int, int]


def irange(left, right):
    if left <= right:
        return range(left, right+1)
    else:
        return range(left, right-1, -1)


orthagonals = [(0, -1), (1, 0), (0, 1), (-1, 0)]
diagonals = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
directions = orthagonals + diagonals

def is_normal(d: Dir) -> bool:
    return all(x in (-1, 0, 1) for x in d)

def is_orthagonal(d: Dir) -> bool:
    return any(x == 0 for x in d)

def is_diagonal(d: Dir) -> bool:
    return not is_orthagonal(d)

def offset(p: Point, d: Dir) -> Point:
    return p[0]+d[0], p[1]+d[1]

def invert(d: Dir) -> Dir:
    return -d[0], -d[1]


class Grid(Generic[T]):
    data: list[T]

    def __init__(self, w: int, h: int, l: T | list[T]):
        self.width = w
        self.height = h
        if isinstance(l, list):
            if w*h != len(l):
                raise ValueError(f"{w}*{h} = {w*h} but only {len(l)} elements provided")
            self.data = l
        else:
            self.data = [l for _ in range(w*h)]

    def orthagonals(self, p: Point):
        for d in orthagonals:
            yield offset(p, d)

    def adjacent(self, p: Point):
        for d in directions:
            yield offset(p, d)

    def __len__(self) -> int:
        return self.width*self.height

    def __contains__(self, p: Point) -> bool:
        return 0 <= p[0] < self.width and 0 <= p[1] < self.height

    def __getitem__(self, p: Point) -> Optional[T]:
        if p not in self:
            return None
        return self.data[p[1]*self.width+p[0]]

    def __setitem__(self, p: Point, x: T):
        if p not in self:
            raise IndexError(f"assigning to out of bounds point {p}")
        self.data[p[1]*self.width+p[0]] = x

    def __iter__(self) -> Iterator[Point]:
        return ((x, y) for y in range(self.height) for x in range(self.width))

    def _repr(self, f: Callable[[object], str]) -> str:
        m = self.copy().map(f)
        l = max(map(len, m.values()))
        s = []
        st = ""
        for row in m.rows():
            for v in m.take(row):
                st += f"{v:>{l}} "
            s.append(st)
            st = ""
        return "\n" + "\n".join(s) + "\n"

    def __repr__(self) -> str:
        return self._repr(repr)

    def __str__(self) -> str:
        return self._repr(str)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Grid):
            return NotImplemented
        return (self.width, self.height, self.data) == (other.width, other.height, other.data)

    def __hash__(self) -> int:
        return hash((self.width, self.height, tuple(self.data)))

    def count(self, pred: Callable[[T], int] = lambda _: 1) -> int:
        return sum(pred(x) for x in self.values())

    def take(self, ps: Iterable[Point]) -> list[T]:
        l = []
        for p in ps:
            if p not in self:
                raise IndexError(f"out of bounds point {p} in take sequence")
            l.append(self[p])
        return l

    def values(self) -> list[T]:
        return self.take(self)

    def map(self, f: Callable[[T], G]) -> Grid[G]:
        for i in range(len(self.data)):
            self.data[i] = f(self.data[i])  # type: ignore
        return self  # type: ignore

    def copy(self) -> Grid[T]:
        return type(self)(self.width, self.height, self.data.copy())

    def rows(self) -> list[list[Point]]:
        return [[(x, y) for x in range(self.width)] for y in range(self.height)]

    def columns(self) -> list[list[Point]]:
        return [[(x, y) for y in range(self.height)] for x in range(self.width)]

    def blit(self, point: Point, other: Grid[T]) -> Grid[T]:
        for p in other:
            try:
                self[offset(p, point)] = other[p]  # type: ignore
            except IndexError:
                pass
        return self

    def concat(self, *others: Grid[T]) -> Grid[T]:
        summands = self, *others
        width = sum(x.width for x in summands)
        height = self.height
        r: Grid[T | None] = Grid(width, height, None)
        o = 0
        for grid in summands:
            if grid.height != height:
                raise ValueError("concat arguments differ in height")
            for x, y in grid:
                r[x+o, y] = grid[x, y]
            o += grid.width
        return r  # type: ignore

    def vconcat(self, *others: Grid[T]) -> Grid[T]:
        summands = self, *others
        width = self.width
        height = sum(x.height for x in summands)
        r: Grid[T | None] = Grid(width, height, None)
        o = 0
        for grid in summands:
            if grid.width != width:
                raise ValueError("vconcat arguments differ in width")
            for x, y in grid:
                r[x, y+o] = grid[x, y]
            o += grid.height
        return r  # type: ignore

    def flip(self) -> Grid[T]:
        for y in range(self.height):
            for x in range(self.width//2):
                them = self.width-x-1, y
                self[x, y], self[them] = self[them], self[x, y]  # type: ignore
        return self

    def vflip(self) -> Grid[T]:
        for x in range(self.width):
            for y in range(self.height//2):
                them = x, self.height-y-1
                self[x, y], self[them] = self[them], self[x, y]  # type: ignore
        return self

    def rot(self) -> Grid[T]:
        w = self.height
        h = self.width
        grid: Grid[T | None] = Grid(w, h, None)
        for x, y in self:
            grid[w-y-1, x] = self[x, y]
        return grid  # type: ignore

    def lrot(self) -> Grid[T]:
        w = self.height
        h = self.width
        grid: Grid[T | None] = Grid(w, h, None)
        for x, y in self:
            grid[y, h-x-1] = self[x, y]
        return grid  # type: ignore

    @classmethod
    def parse(cls, s: str, convert: Callable[[str], T], split: Callable[[str], Iterable[str]] = list) -> Grid[T]:
        return cls.from_list(map(convert, split(r)) for r in s.splitlines())

    @classmethod
    def from_list(cls, l: Iterable[Iterable[T]]) -> Grid[T]:
        if not l:
            raise ValueError("empty list")
        w = None
        h = 0
        data = []
        for row in l:
            ln = 0
            for x in row:
                data.append(x)
                ln += 1
            if w is None:
                w = ln
            elif ln != w:
                raise ValueError("inconsistent row lengths")
            h += 1
        assert w is not None
        return cls(w, h, data)

    def to_list(self) -> list[list[T]]:
        return [[self.data[y*self.width+x] for x in range(self.width)] for y in range(self.height)]

from __future__ import annotations

import itertools
import functools
from typing import TypeVar, Callable, Any, Generic, Optional, Iterable, Iterator, Mapping


__all__ = (
    "orthagonals", "diagonals", "directions",
    "is_normal", "is_orthagonal", "is_diagonal",
    "offset", "invert", "Grid", "SparseGrid",
)


T = TypeVar("T")
G = TypeVar("G")
Dir = tuple[int, int]
Point = tuple[int, int]


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

    def __init__(self, w: int, h: int, l: T | Callable[[int, int], T] | list[T]):
        self.width = w
        self.height = h
        if isinstance(l, list):
            if w*h != len(l):
                raise ValueError(f"{w}*{h} = {w*h} but only {len(l)} elements provided")
            self.data = l
        elif callable(l):
            self.data = [l(x, y) for y in range(h) for x in range(w)]
        else:
            self.data = [l for _ in range(w*h)]

    @staticmethod
    def orthagonals(p: Point):
        for d in orthagonals:
            yield offset(p, d)

    @staticmethod
    def adjacent(p: Point):
        for d in directions:
            yield offset(p, d)

    def __len__(self) -> int:
        return self.width*self.height

    def __contains__(self, p: Point) -> bool:
        return 0 <= p[0] < self.width and 0 <= p[1] < self.height

    def get_unchecked(self, p: Point) -> T:
        return self.data[p[1]*self.width+p[0]]

    def __getitem__(self, p: Point) -> Optional[T]:
        if p not in self:
            return None
        return self.get_unchecked(p)

    def __setitem__(self, p: Point, x: T):
        if p not in self:
            raise IndexError(f"assigning to out of bounds point {p}")
        self.data[p[1]*self.width+p[0]] = x

    def __iter__(self) -> Iterator[Point]:
        return ((x, y) for y in range(self.height) for x in range(self.width))

    def _repr(self, f: Callable[[object], str]) -> str:
        if not self.data:
            return "<empty grid>"
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
        for i, x in enumerate(self.data):
            self.data[i] = f(x)  # type: ignore
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
                self[offset(p, point)] = other.get_unchecked(p)
            except IndexError:
                pass
        return self

    def concat(*summands: Grid[T]) -> Grid[T]:
        width = sum(x.width for x in summands)
        height = summands[0].height if summands else 0
        r: Grid[T] = Grid(width, height, None)  # type: ignore
        o = 0
        for grid in summands:
            if grid.height != height:
                raise ValueError("concat arguments differ in height")
            for x, y in grid:
                r[x+o, y] = grid.get_unchecked((x, y))
            o += grid.width
        return r

    def vconcat(*summands: Grid[T]) -> Grid[T]:
        width = summands[0].width if summands else 0
        height = sum(x.height for x in summands)
        r: Grid[T] = Grid(width, height, None)  # type: ignore
        o = 0
        for grid in summands:
            if grid.width != width:
                raise ValueError("vconcat arguments differ in width")
            for x, y in grid:
                r[x, y+o] = grid.get_unchecked((x, y))
            o += grid.height
        return r

    def flip(self) -> Grid[T]:
        for y in range(self.height):
            for x in range(self.width//2):
                us = x, y
                them = self.width-x-1, y
                self[us], self[them] = self.get_unchecked(them), self.get_unchecked(us)
        return self

    def vflip(self) -> Grid[T]:
        for x in range(self.width):
            for y in range(self.height//2):
                us = x, y
                them = x, self.height-y-1
                self[us], self[them] = self.get_unchecked(them), self.get_unchecked(us)
        return self

    def rot(self) -> Grid[T]:
        w = self.height
        h = self.width
        return Grid(w, h, lambda x, y: self.get_unchecked((y, h-x-1)))

    def lrot(self) -> Grid[T]:
        w = self.height
        h = self.width
        return Grid(w, h, lambda x, y: self.get_unchecked((w-y-1, x)))

    @classmethod
    def parse(cls, s: str) -> Grid[str]:
        return cls.from_list(s.splitlines())

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

    @classmethod
    def from_dict(cls, d: Mapping[Point, T]) -> Grid[T]:
        if not d:
            return cls(0, 0, None)
        min_x = float("inf")
        max_x = float("-inf")
        min_y = float("inf")
        max_y = float("-inf")
        for x, y in d.keys():
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
        return Grid(max_x-min_x+1, max_y-min_y+1, lambda x, y: d[x+min_x, y+min_y])  # type: ignore

    def tile(self) -> SparseGrid[T]:
        return SparseGrid(lambda p: self.get_unchecked((p[0] % self.width, p[1] % self.height)))

    def isolate(self, using: G) -> SparseGrid[T | G]:
        return SparseGrid(lambda _: using, {p: self.get_unchecked(p) for p in self})


class SparseGrid(Generic[T], dict[Point, T]):
    def __init__(self, f: Callable[[Point], T], *args, **kwargs):
        self.f = f
        super().__init__(*args, **kwargs)

    def __missing__(self, key: Point) -> T:
        return self.f(key)

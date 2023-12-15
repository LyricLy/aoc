from __future__ import annotations

import re
import sys

from .grid import Grid


class UsageError(Exception):
    pass

def extract_nums(s: object) -> list[int]:
    return [int(x) for x in re.findall(r"-?\d+", str(s))]

class Aoc:
    def __init__(self, string: str):
        self.string = string.strip()

    def __repr__(self):
        return self.string

    def __eq__(self, other):
        if isinstance(other, str):
            return self.string == other
        if isinstance(other, Aoc):
            return self.string == other.string
        return NotImplemented

    def __hash__(self):
        return hash(self.string)

    def _section(self) -> str:
        for x in ["\n\n", "\n"]:
            if x in self.string:
                return x
        return ""

    @property
    def items(self) -> list[Aoc]:
        if s := self._section():
            return self.split(s)

        for x in ["|", "->", ";", ",", "=", "-", " "]:
            if x in self.body:
                return self.split(x)

        raise UsageError("can't split into items")

    @property
    def dechaff(self) -> list[list[Aoc]]:
        rows = [re.split(r"\b", x.string) for x in self.items]
        bads = {i for i, col in enumerate(zip(*rows)) if len(set(col)) == 1}
        rs = []
        for row in rows:
            r = [""]
            for i, word in enumerate(row):
                if i in bads:
                    if r[-1]:
                        r.append("")
                    continue
                r[-1] += word
            if not r[-1]:
                r.pop()
            rs.append([Aoc(x) for x in r])
        return rs

    @property
    def words(self) -> list[str]:
        return self.body.split()

    @property
    def nums(self) -> list[int]:
        return extract_nums(self.body)

    @property
    def num(self) -> int:
        l = self.nums
        if len(l) != 1:
            raise UsageError("must be exactly one number for num")
        return l[0]

    def split(self, sep: str | None) -> list[Aoc]:
        return [Aoc(x) for x in self.body.split(sep)]

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, i):
        if isinstance(i, int):
            return self.items[i]
        if isinstance(i, str):
            try:
                v = self.val_map
            except:
                return self.header_map[i]
            else:
                return v[i]  # type: ignore

    def __len__(self):
        return len(self.items)

    def _header_and_body(self) -> tuple[str, str] | None:
        split = ":" + self._section()
        if split not in self.string:
            return None
        x, y = self.string.split(":", 1)
        return x.strip(), y.strip()

    @property
    def header(self) -> str:
        if not (r := self._header_and_body()):
            raise UsageError("can't find header")
        return r[0]

    @property
    def body(self) -> str:
        if not (r := self._header_and_body()):
            return self.string
        return r[1]

    @property
    def id(self) -> int:
        ns = extract_nums(self.header)
        if len(ns) != 1:
            raise UsageError("id not known")
        return ns[0]

    @property
    def header_map(self) -> dict[str, Aoc]:
        return {x.header: x for x in self.items}

    @property
    def id_map(self) -> dict[int, Aoc]:
        return {x.id: x for x in self.items}

    @property
    def val_map(self) -> dict[Aoc, Aoc]:
        return dict(self.items)  # type: ignore

    @property
    def grid(self) -> Grid[str]:
        return Grid.parse(self.body, lambda x: x)

def get_input():
    with open(sys.argv[1]) as f:
        return Aoc(f.read())

import requests
import re
import sys
import os
import time
import importlib
import traceback
import datetime
import argparse
from collections import defaultdict
from zoneinfo import ZoneInfo

sys.path.append(os.getcwd())

with open("session") as f:
    token = f.read().strip()
session = requests.Session()
session.headers.update({"User-Agent": "https://github.com/LyricLy/aoc (christinahansondesu@gmail.com)", "Cookie": f"session={token}"})

def get_example(year, day, part):
    path = f"./inputs/ex{year}-{day}-{part}"
    try:
        with open(path) as f:
            g, x = f.read().split("::*::")
    except FileNotFoundError:
        s = session.get(f"https://adventofcode.com/{year}/day/{day}").text
        regex = r"For example.*?:.*?<pre><code>(.*?)</code></pre>.*?<code><em>(.*?)</em></code>" if part == 1 else r"For example.*?:.*?<pre><code>(.*?)</code></pre>.*?Part Two.*<code><em>(.*?)</em></code>"
        if not (m := re.search(regex, s, re.DOTALL)):
            return None
        g, x = m.groups()
        x = input(f"Example answer ({x}): ") or x
        if not g.endswith("\n"):
            g = f"{g}\n"
        with open(path, "w") as f:
            f.write(f"{g}::*::{x}")
    return g, int(x) if x.isdigit() else x

def get_input(year, day):
    path = f"./inputs/{year}-{day}"
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        pass
    s = session.get(f"https://adventofcode.com/{year}/day/{day}/input").text
    if s.endswith("\n\n"):
        s = s.removesuffix("\n")
    with open(path, "w") as f:
        f.write(s)
    return s

wrong = defaultdict(set)
part_one = None
def submit(year, day, part, data, wanted_type):
    global part_one
    if not isinstance(data, wanted_type) or data in ("", "None"):
        return print(f"{data!r} is not an answer, refusing")
    data = str(data)
    if data in wrong[year, day, part]:
        return print(f"{data} was tried already, refusing")
    if part == 2 and part_one is not None and data == part_one:
        return print(f"{data} was part 1 answer, refusing")
    print(f"trying {data}")
    r = session.post(f"https://adventofcode.com/{year}/day/{day}/answer", data={"level": part, "answer": data})
    print(r.text)
    if "That's not the right answer." in r.text:
        wrong[year, day, part].add(data)
        print("no good, sleeping off")
        time.sleep(60)
    elif "You gave an answer too recently" in r.text:
        print("moved too quickly. sleeping difference")
        m, s = re.search(r"You have (?:(\d+)m )?(\d+)s left to wait", r.text).groups()
        time.sleep((int(m) if m else 0)*60+int(s))
    elif "That's the right answer" in r.text:
        if part == 1:
            part_one = data
        print("got it!")
        return True


def do_day(year, day, part_start, file):
    for part in range(part_start, 3):
        last = os.stat(file).st_mtime
        skip = False
        print(f"starting part {part}")
        while True:
            t = os.stat(file).st_mtime
            if t != last or skip:
                last = t
                try:
                    mod = importlib.reload(importlib.import_module(file.removesuffix(".py")))
                except:
                    print("solution doesn't compile, refusing")
                    traceback.print_exc()
                    continue
                if e := get_example(year, day, part):
                    g, x = e
                    try:
                        if (v := mod.go(g)) != x:
                            print(f"failed example (wanted {x}, got {v}), refusing")
                            continue
                    except:
                        print("caught exception while testing, refusing")
                        traceback.print_exc()
                        continue
                try:
                    if submit(year, day, part, mod.go(get_input(year, day)), type(x)):
                        break
                except:
                    print("caught exception, refusing")
                    traceback.print_exc()
                    continue

if __name__ == "__main__":
    now = datetime.datetime.now(ZoneInfo("America/New_York"))
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", default="thing.py")
    parser.add_argument('-y', '--year', type=int, default=now.year)
    parser.add_argument('-d', '--day', type=int, default=now.day)
    parser.add_argument('-p', '--part', type=int, default=1)
    args = parser.parse_args()
    do_day(args.year, args.day, args.part, args.filename)

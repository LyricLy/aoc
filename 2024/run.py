import re
import datetime
import os
import html
import sys
import subprocess
from zoneinfo import ZoneInfo

import requests


now = datetime.datetime.now(ZoneInfo("America/New_York"))

with open("session") as f:
    token = f.read().strip()
session = requests.Session()
session.headers.update({"User-Agent": "https://github.com/LyricLy/aoc (christinahansondesu@gmail.com)", "Cookie": f"session={token}"})

if not os.path.exists("example.txt"):
    s = session.get(f"https://adventofcode.com/{now.year}/day/{now.day}").text
    regex = r"For example[^\n]*?:</p>\s*<pre><code>(.*?)</code></pre>"
    if m := re.search(regex, s, re.DOTALL):
        with open("example.txt", "w") as f:
            f.write(html.unescape(m[1]))
    else:
        print("no example found, not writing", file=sys.stderr)

if not os.path.exists("input.txt"):
    s = session.get(f"https://adventofcode.com/{now.year}/day/{now.day}/input").text
    with open("input.txt", "w") as f:
        f.write(s)

subprocess.run(["python", "thing.py", "example.txt" if len(sys.argv) <= 1 else "input.txt"])

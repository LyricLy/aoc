from common import *
import networkx
from networkx.drawing.nx_pydot import write_dot
a = get_input()
g = networkx.Graph()
for x, ys in a.header_map.items():
    for y in ys.split(" "):
        g.add_edge(x, y.string)
g.remove_edge("fht", "vtt")
g.remove_edge("bbg", "kbr")
g.remove_edge("czs", "tdk")
import math
print(math.prod(len(x) for x in networkx.connected_components(g)))

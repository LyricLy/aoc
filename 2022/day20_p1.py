from tqdm import tqdm
example = 0

with open("example.txt" if example else "input.txt") as f:
    t = f.read()

data = [int(x) for x in t.splitlines()]

class Node:
    def __init__(self, n, left, right):
        self.n = n
        self.left = left
        self.right = right

    def beat(self):
        if self.n < 0:
            for _ in range(-self.n):
                self.left.left.right, self.left.left, self.right.left, self.left.right, self.right, self.left = self, self, self.left, self.right, self.left, self.left.left
        else:
            for _ in range(self.n):
                self.right.right.left, self.right.right, self.left.right, self.right.left, self.left, self.right = self, self, self.right, self.left, self.right, self.right.right

    def __repr__(self):
        return f"({self.left.n} < {self.n} > {self.right.n})"

nodes = []
for n in data:
    left = nodes[-1] if nodes else None
    us = Node(n, left, None)
    nodes.append(us)
    if left:
        left.right = us
nodes[0].left = nodes[-1]
nodes[-1].right = nodes[0]

for node in tqdm(nodes):
    node.beat()

for node in nodes:
    if node.n == 0:
        break
new_list = [node.n]
next_node = node
while (next_node := next_node.right) != node:
    new_list.append(next_node.n)

s = 0
for i in (1000, 2000, 3000):
    s += new_list[i%len(new_list)]
print(s)

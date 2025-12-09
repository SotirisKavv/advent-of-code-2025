from math import dist, prod

class UnionFind:
    def __init__(self, items):
        self.parent = {item: item for item in items}
        self.size = {item: 1 for item in items}
    
    def find(self, item):
        if item not in self.parent:
            self.parent[item] = item
            self.size[item] = 1
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, item1, item2):
        root1 = self.find(item1)
        root2 = self.find(item2)
        
        if root1 != root2:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
            del self.size[root2]
    
    def set_sizes(self):
        return list(self.size.values())

with open("junctions.txt") as f:
    lines = f.readlines()
    junctions = [tuple(map(int, line.strip().split(","))) for line in lines]
    
distances = [[j1, j2, dist(j1, j2)] for i, j1 in enumerate(junctions) for j2 in junctions[i+1:]]
distances.sort(key=lambda x: x[2])

uf = UnionFind(junctions)

for i, (j1, j2, d) in enumerate(distances):
    if uf.find(j1) != uf.find(j2):
        uf.union(j1, j2)

    if len(uf.set_sizes()) == 1:
        print(j1[0] * j2[0])
        break


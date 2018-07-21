
from collections import defaultdict


class Graph:

    def __init__(self, vertices):

        # No. of vertices
        self.vertices = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, src, target, maxDepth):

        if src == target: return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0: return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            if self.dfs(i, target, maxDepth - 1):
                print(i)
                return True
        return False

    def iddfs(self, src, target, maxDepth):
        for i in range(maxDepth):
            if self.dfs(src, target, i):
                return True
        return False


# Create a graph given in the above diagram
g = Graph(7);
g.add_edge(0, 1)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 1)
g.add_edge(1, 4)
g.add_edge(4, 1)
g.add_edge(2, 5)
g.add_edge(5, 2)
g.add_edge(2, 6)
g.add_edge(6, 2)

target = 6
maxDepth = 300
src = 3

if g.iddfs(src, target, maxDepth) == True:
    print("Target is reachable from source " +
          "within max depth")
else:
    print("Target is NOT reachable from source " +
          "within max depth")

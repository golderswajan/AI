from collections import defaultdict as my_dict

path = list()
limit = 0


class ANTF_Solver:

    def __init__(self):
        self.graph = my_dict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start, max_depth, visited):
        if not visited[start]:
            path.append(start)
        visited[start] = True
        if max_depth <= 0:
            return False

        for i in self.graph[start]:
            if self.dfs(i, max_depth - 1, visited):
                return True
        return False

    def iddfs(self, start, max_depth):
        global limit
        limit = len(self.graph)
        visited = dict()
        for v in self.graph.keys():
            visited[v] = False
        for i in range(max_depth + 1):
            if self.dfs(start, i, visited):
                return True
        return False


""" Program Starts Here """
case = 0
while True:

    try:
        g = ANTF_Solver()
        n = int(input())
        if not n:
            break
    except EOFError:
        break

    for x in range(n):
        try:
            src, TTL = map(int, input().split())
            g.add_edge(src, TTL)
        except EOFError:
            break

    while True:
        try:
            s, ttl = map(int, input().split())
            if not s or not ttl:
                break
        except EOFError:
            break
        g.iddfs(s, ttl)
        case = case + 1
        # print(path)
        print("Case %d: %d nodes not reachable from node %d with TTL = %d." % (case, limit - len(path), s, ttl))
        path.clear()

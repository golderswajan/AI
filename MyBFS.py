class Node:

    def __init__(self, no, value='', adjacent=list()):
        self.no = no
        self.value = value
        if not adjacent:
            self.adjacent = list()
        else:
            self.adjacent = adjacent
        self.visited = False

    def set_value(self, value):
        self.value = value

    def add_adjacent(self, adjacent):
        for i in adjacent:
            self.adjacent.append(i)

    def visit(self):
        self.visited = True

    def __repr__(self):
        return 'no -> ' + str(self.no) + '\n' + \
               'value -> ' + str(self.value) + '\n' + \
               'adjacent -> ' + str(self.adjacent) + '\n' + \
               'visited -> ' + str(self.visited) + '\n'


def bfs(node_no):
    queue = list()
    node = graph[node_no]
    node.visit()
    queue.append(node_no)
    while queue:
        node_no = queue.pop()
        node = graph[node_no]
        print(node_no)

        for adj in node.adjacent:
            if not graph[adj].visited:
                graph[adj].visit()
                queue.insert(0, adj)


node_number = 9
graph = [Node(i) for i in range(node_number)]
graph[0].add_adjacent([1, 5])
graph[1].add_adjacent([2])
graph[2].add_adjacent([3, 4])
graph[5].add_adjacent([6, 7])
graph[7].add_adjacent([8])
bfs(0)
# print(graph)
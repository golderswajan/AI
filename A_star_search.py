class Node:

    def __init__(self, no, value='', adjacent=list(), adj_cost=list(), straight_cost=0):
        self.no = no
        self.value = value
        if not adjacent:
            self.adjacent = list()
        else:
            self.adjacent = adjacent
        if not adj_cost:
            self.adj_cost = list()
        else:
            self.adj_cost = adj_cost
        self.straight_cost = straight_cost
        self.new_adj_cost = 0
        self.total_cost = 0
        self.parents = list()
        self.visited = False

    def set_value(self, value):
        self.value = value

    def set_straight_cost(self, value):
        self.straight_cost = value

    def set_new_adj_cost(self, value):
        self.new_adj_cost = value

    def set_total_cost(self, value):
        self.total_cost = value

    def set_parents(self, parents):
        self.parents = parents

    def add_adjacent(self, adjacent):
        for i in adjacent:
            self.adjacent.append(i)

    def add_adjacent_cost(self, adjacent_cost):
        for i in adjacent_cost:
            self.adj_cost.append(i)

    def add_parents(self, parents):
        if type(parents) is list:
            for i in parents:
                self.parents.append(i)
        else:
            self.parents.append(parents)

    def visit(self):
        self.visited = True

    def __repr__(self):
        return 'no -> ' + str(self.no) + '\n' + \
               'value -> ' + str(self.value) + '\n' + \
               'adjacent -> ' + str(self.adjacent) + '\n' + \
               'adjacent cost -> ' + str(self.adj_cost) + '\n' + \
               'straight cost -> ' + str(self.straight_cost) + '\n' + \
               'new adj cost -> ' + str(self.new_adj_cost) + '\n' + \
               'total cost -> ' + str(self.total_cost) + '\n' + \
               'parent -> ' + str(self.parent) + '\n' + \
               'visited -> ' + str(self.visited) + '\n'


def dfs(node_no):
    global movable_nodes, x, target
    x += 1
    node = graph[node_no]
    node.visit()
    # print(node.no)
    current_adj = list()
    for adj in node.adjacent:
        if not graph[adj].visited:
            temp_cost = graph[adj].total_cost
            graph[adj].set_new_adj_cost(node.new_adj_cost + node.adj_cost[node.adjacent.index(adj)])
            # print(node.adj_cost[node.adjacent.index(adj)])
            graph[adj].set_total_cost(graph[adj].new_adj_cost + graph[adj].straight_cost)
            if adj not in movable_nodes:
                graph[adj].add_parents(node.parents)
                graph[adj].add_parents(node_no)
            else:
                if graph[adj].total_cost < temp_cost:
                    graph[adj].set_parents(node.parents)
                    graph[adj].add_parents(node_no)

            print(graph[adj].total_cost)
            movable_nodes.append(adj)
            current_adj.append(adj)
            # print(adj)
    movable_nodes.sort(key=lambda z: graph[z].total_cost)

    print(movable_nodes)
    print('\n')
    if target in movable_nodes and graph[movable_nodes[0]].total_cost == graph[target].total_cost:
        return
    min_node_no= movable_nodes[0]
    movable_nodes.pop(0)

    # if not current_adj and min_node_no not in current_adj:
    #     temp_current_adj = current_adj[0]
    #     while graph[min_node_no].parent != graph[temp_current_adj]:
    #         temp_current_adj = graph[temp_current_adj]
    #         path.pop()
    #
    # path.append(min_node_no)
    dfs(min_node_no)


movable_nodes = list()
path = list()
x = 0
node_number = 6
graph = [Node(i) for i in range(node_number)]
graph[0].add_adjacent([1])
graph[0].add_adjacent_cost([140])
graph[0].set_straight_cost(366)
graph[0].set_total_cost(366)

graph[1].add_adjacent([0, 2, 3])
graph[1].add_adjacent_cost([140, 99, 80])
graph[1].set_straight_cost(253)

graph[2].add_adjacent([1, 5])
graph[2].add_adjacent_cost([99, 211])
graph[2].set_straight_cost(176)

graph[3].add_adjacent([1, 4])
graph[3].add_adjacent_cost([80, 97])
graph[3].set_straight_cost(193)

graph[4].add_adjacent([3, 5])
graph[4].add_adjacent_cost([97, 101])
graph[4].set_straight_cost(100)

graph[5].add_adjacent([2, 4])
graph[5].add_adjacent_cost([211, 101])
graph[5].set_straight_cost(0)

src = 0
target = 5
dfs(0)
print(graph[5].parents)
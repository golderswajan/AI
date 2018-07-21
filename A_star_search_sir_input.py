class Node:

    def __init__(self, no, name='', adjacent=list(), adj_cost=list(), straight_cost=0):
        self.no = no
        self.name = name
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

    def set_name(self, name):
        self.name = name

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


def a_star(node_no):
    global move_able_nodes, target
    node = graph[node_no]
    node.visit()
    # print(node.no)
    current_adj = list()
    for adj in node.adjacent:
        if not graph[adj].visited:
            temp_new_adj_cost = node.new_adj_cost + node.adj_cost[node.adjacent.index(adj)]
            temp_total_cost = temp_new_adj_cost + graph[adj].straight_cost

            if adj not in move_able_nodes:
                graph[adj].set_new_adj_cost(temp_new_adj_cost)
                graph[adj].set_total_cost(temp_total_cost)
                graph[adj].add_parents(node.parents)
                graph[adj].add_parents(node_no)
            else:
                if graph[adj].total_cost > temp_total_cost:
                    graph[adj].set_new_adj_cost(temp_new_adj_cost)
                    graph[adj].set_total_cost(temp_total_cost)
                    graph[adj].set_parents(node.parents)
                    graph[adj].add_parents(node_no)

            # print(graph[adj].total_cost)
            move_able_nodes.append(adj)
            current_adj.append(adj)
            # print(adj)
    move_able_nodes.sort(key=lambda z: graph[z].total_cost)

    if target in move_able_nodes and graph[move_able_nodes[0]].total_cost == graph[target].total_cost:
        return
    min_node_no = move_able_nodes[0]
    move_able_nodes.pop(0)
    a_star(min_node_no)


move_able_nodes = list()
node_number = 20
graph = [Node(i) for i in range(node_number)]

graph[0].set_name('Arad')
graph[0].add_adjacent([1, 3, 4])
graph[0].add_adjacent_cost([75, 118, 140])
graph[0].set_straight_cost(366)
graph[0].set_total_cost(366)

graph[1].set_name('Zerind')
graph[1].add_adjacent([0, 2])
graph[1].add_adjacent_cost([75, 71])
graph[1].set_straight_cost(374)

graph[2].set_name('Oradea')
graph[2].add_adjacent([1, 4])
graph[2].add_adjacent_cost([71, 151])
graph[2].set_straight_cost(380)

graph[3].set_name('Timisoara')
graph[3].add_adjacent([0, 6])
graph[3].add_adjacent_cost([118, 111])
graph[3].set_straight_cost(329)

graph[4].set_name('Sibiu')
graph[4].add_adjacent([0, 2, 5, 7])
graph[4].add_adjacent_cost([140, 151, 99, 80])
graph[4].set_straight_cost(253)

graph[5].set_name('Fagaras')
graph[5].add_adjacent([4, 12])
graph[5].add_adjacent_cost([99, 211])
graph[5].set_straight_cost(176)

graph[6].set_name('Lugoj')
graph[6].add_adjacent([3, 9])
graph[6].add_adjacent_cost([111, 70])
graph[6].set_straight_cost(244)

graph[7].set_name('Rimniku Vilcia')
graph[7].add_adjacent([4, 8, 11])
graph[7].add_adjacent_cost([80, 97, 146])
graph[7].set_straight_cost(193)

graph[8].set_name('Pitesti')
graph[8].add_adjacent([7, 11, 12])
graph[8].add_adjacent_cost([97, 146, 101])
graph[8].set_straight_cost(100)

graph[9].set_name('Mehedia')
graph[9].add_adjacent([6, 10])
graph[9].add_adjacent_cost([70, 75])
graph[9].set_straight_cost(241)

graph[10].set_name('Dobereta')
graph[10].add_adjacent([9, 11])
graph[10].add_adjacent_cost([75, 120])
graph[10].set_straight_cost(242)

graph[11].set_name('Cralova')
graph[11].add_adjacent([7, 8, 10])
graph[11].add_adjacent_cost([146, 138, 120])
graph[11].set_straight_cost(160)

graph[12].set_name('Bucharest')
graph[12].add_adjacent([5, 8, 13, 14])
graph[12].add_adjacent_cost([211, 101, 90, 85])
graph[12].set_straight_cost(0)

graph[13].set_name('Glurglu')
graph[13].add_adjacent([0])
graph[13].add_adjacent_cost([90])
graph[13].set_straight_cost(77)

graph[14].set_name('Urziceni')
graph[14].add_adjacent([12, 15, 17])
graph[14].add_adjacent_cost([85, 98, 142])
graph[14].set_straight_cost(80)

graph[15].set_name('Hirsova')
graph[15].add_adjacent([14, 16])
graph[15].add_adjacent_cost([98, 86])
graph[15].set_straight_cost(151)

graph[16].set_name('Efroi')
graph[16].add_adjacent([15])
graph[16].add_adjacent_cost([86])
graph[16].set_straight_cost(161)

graph[17].set_name('Vaslui')
graph[17].add_adjacent([14, 18])
graph[17].add_adjacent_cost([142, 92])
graph[17].set_straight_cost(199)

graph[18].set_name('Iasi')
graph[18].add_adjacent([17, 19])
graph[18].add_adjacent_cost([92, 87])
graph[18].set_straight_cost(226)

graph[19].set_name('Neamt')
graph[19].add_adjacent([18])
graph[19].add_adjacent_cost([87])
graph[19].set_straight_cost(234)

src = 0
target = 12
a_star(src)
graph[target].parents.append(target)
print([graph[x].name for x in graph[target].parents])
print('Total Cost : ', graph[target].total_cost)

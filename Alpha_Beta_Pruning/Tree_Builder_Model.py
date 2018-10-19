from ete3 import Tree, TreeStyle, NodeStyle, TextFace


class TreeBuilder:
    def __init__(self, data, alpha_beta_object):
        self.data = data
        self.alpha_beta_object = alpha_beta_object
        self.tree = None

    def build_tree_structure(self):
        tree_structure = list(self.data) #['.' for i in range(len(self.data))]
        tree_structure.reverse()
        # print(tree_structure)
        branch_factor = self.alpha_beta_object.branch_factor
        while len(tree_structure) != 1:
            temp = list()
            for i in range(0, len(tree_structure), branch_factor):
                pair = '('
                for j in range(i, i+branch_factor):
                    pair += str(tree_structure[j])
                    if j != i+branch_factor-1:
                        pair += ','
                pair += ')'
                temp.append(pair)
            tree_structure = temp
            # print(tree_structure)
        tree_structure = tree_structure[0] + ';'
        # print(tree_structure)
        self.tree = Tree(tree_structure)

    def populate_tree_with_pruned_data(self):
        tree_data = self.alpha_beta_object.tree_data
        pruned_data = self.alpha_beta_object.pruned_data
        depth = self.alpha_beta_object.depth
        branch_factor = self.alpha_beta_object.branch_factor
        adjusted_tree_data = list(list() for i in range(depth+1))
        pruned_list = list()
        pruned_string = list()

        for row in range(depth+1):
            pruned_tree_index = 0
            for index in range(branch_factor ** row):
                if index in pruned_list:
                    adjusted_tree_data[row].append('')
                else:
                    adjusted_tree_data[row].append(tree_data[row][pruned_tree_index])
                    pruned_tree_index += 1
                # pruned parents' child calculation after a depth complete
                if index == branch_factor ** row - 1:
                    temp_pruned_list = list()
                    for item in pruned_list:
                        for i in range(item * branch_factor, item * branch_factor + branch_factor):
                            temp_pruned_list.append(i)
                    pruned_list = temp_pruned_list
            # pruned child calculation for the next level
            if pruned_data[row]:
                for item in pruned_data[row]:
                    start = item['node'] * branch_factor
                    for index, i in enumerate(range(start + item['index'] + 1, start + branch_factor)):
                        pruned_list.append(i)
                        pruned_string_position = node_count(branch_factor, row) + branch_factor**(row+1)-(item['node']*branch_factor+item['index']+index+1)-1
                        pruned_string.append(pruned_string_position)

        print('adjusted',adjusted_tree_data)
        print(pruned_string)
        # adjusted_tree_data[-1] = self.data
        [row.reverse() for row in adjusted_tree_data]
        # print(adjusted_tree_data)
        adjusted_tree_data = sum(adjusted_tree_data, [])
        # print(adjusted_tree_data)

        limiter = node_count(branch_factor, depth-1)
        for index, node in enumerate(self.tree.traverse()):
            if index<=limiter:
                node.add_face(TextFace(adjusted_tree_data[index]), column=1, position='branch-top')
            if index in pruned_string:
                node.add_face(TextFace('pruned'), column=1, position='branch-top')

    def show_tree(self):
        ts = TreeStyle()
        ts.rotation = 90
        ts.show_scale = False
        ns = NodeStyle()
        ns["shape"] = "sphere"
        ns["size"] = 10
        ns["fgcolor"] = "darkred"
        for node in self.tree.traverse():
            node.set_style(ns)
        self.tree.show(tree_style=ts)

def node_count(branch_factor, depth):
    nodes = 0
    for i in range(depth+1):
        nodes += branch_factor**i
    return nodes
import numpy as np

MAX = np.inf
MIN = -np.inf
# tree_data = list(list() for i in range(4))
# pruned_data = list(list() for i in range(4))


def min_max(depth, node_index, maximizing_player, values, alpha, beta):
    global tree_data, pruned_data
    if depth == 3:
        tree_data[depth].append(values[node_index])
        return values[node_index]

    if maximizing_player:
        best = MIN
        for i in range(2):
            val = min_max(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                pruned_data[depth].append({'node': node_index, 'index': i})
                break
        tree_data[depth].append(best)
        print(tree_data)
        return best
    else:
        best = MAX
        for i in range(2):
            val = min_max(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                pruned_data[depth].append({'node':node_index, 'index':i})
                break
        tree_data[depth].append(best)
        print(tree_data)
        return best


data = [3, 5, 6, 9, 1, 2, 0, -1]
# print("The optimal value is : ", min_max(0, 0, True, data, MIN, MAX))
# tree_data.reverse()
# print(tree_data)
# print(pruned_data)

tree_data = [[5], [5, 2], [5, 6, 2], [3, 5, 6, 1, 2]]
pruned_data = [[], [{'node': 1, 'index': 0}], [{'node': 1, 'index': 0}], []]
adjusted_tree_data = list(list() for i in range(4))
pruned_list = list()
pruned_string_show = list()


for row in range(4):
    pruned_tree_index = 0
    for index in range(2**row):
        if index in pruned_list:
            adjusted_tree_data[row].append('-')
        else:
            adjusted_tree_data[row].append(tree_data[row][pruned_tree_index])
            pruned_tree_index += 1
        # pruned parents' child calculation after a depth complete
        if index == 2**row-1:
            temp_pruned_list = list()
            for item in pruned_list:
                for i in range(item*2, item*2+2):
                    temp_pruned_list.append(i)
            pruned_list = temp_pruned_list
    # pruned child calculation for the next level
    if pruned_data[row]:
        for item in pruned_data[row]:
            start = item['node']*2+item['index']
            for i in range(start+1, start+2):
                pruned_list.append(i)
                pruned_string_show.append(2**(row+1)-1+(2**(row+1)-i)-1)

print(adjusted_tree_data)
[row.reverse() for row in adjusted_tree_data]
print(adjusted_tree_data)
print(sum(adjusted_tree_data,[]))
print(pruned_string_show)


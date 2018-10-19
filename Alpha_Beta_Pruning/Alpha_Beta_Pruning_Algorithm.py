import numpy as np


class AlphaBetaPruning:
    def __init__(self, depth, branch_factor):
        self.depth = depth
        self.branch_factor = branch_factor
        self.tree_data = list(list() for i in range(depth+1))
        self.pruned_data = list(list() for i in range(depth+1))
        self.error_data = list(list() for i in range(depth + 1))
        self.MAX = np.inf
        self.MIN = -np.inf

    def min_max(self, depth, node_index, maximizing_player, values, alpha, beta):
        if depth == self.depth:
            self.tree_data[depth].append(values[node_index])
            self.error_data[depth].append(values[node_index])
            return values[node_index]

        if maximizing_player:
            best = self.MIN
            for i in range(self.branch_factor):
                val = self.min_max(depth + 1, node_index * self.branch_factor + i, False, values, alpha, beta)
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    if i != self.branch_factor - 1:
                        self.pruned_data[depth].append({'node': node_index, 'index': i})
                        self.error_data[depth].append('pruned'+str(i))
                    break
            self.tree_data[depth].append(best)
            self.error_data[depth].append(best)
            # print(self.tree_data)
            return best
        else:
            best = self.MAX
            for i in range(self.branch_factor):
                val = self.min_max(depth + 1, node_index * self.branch_factor + i, True, values, alpha, beta)
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    if i != self.branch_factor - 1:
                        self.pruned_data[depth].append({'node': node_index, 'index': i})
                        self.error_data[depth].append('pruned' + str(i))
                    break
            self.tree_data[depth].append(best)
            self.error_data[depth].append(best)
            # print(self.tree_data)
            return best

    def execute(self, data):
        result = self.min_max(0, 0, True, data, self.MIN, self.MAX)
        return result



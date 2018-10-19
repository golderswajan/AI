from Alpha_Beta_Pruning_Algorithm import AlphaBetaPruning
from Tree_Builder_Model import TreeBuilder
import random as rn

depth = 3
branch_factor = 3
rn.seed(2)
leaf_nodes = [rn.randrange(-10, 10) for i in range(branch_factor**depth)]
# leaf_nodes = [3, 5, 6, 9, -1, 2, 0, -1]
# print(leaf_nodes)


my_alpha_beta = AlphaBetaPruning(depth, branch_factor)
result = my_alpha_beta.execute(leaf_nodes)
# print(result)
print(my_alpha_beta.tree_data)
print(my_alpha_beta.pruned_data)
print(my_alpha_beta.error_data)
my_tree_builder = TreeBuilder(leaf_nodes, my_alpha_beta)
my_tree_builder.build_tree_structure()

my_tree_builder.populate_tree_with_pruned_data()
my_tree_builder.show_tree()

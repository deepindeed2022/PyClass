import numpy as np
from sklearn import tree
from sklearn.utils import shuffle

def load_data(filename="testdata.txt"):
	with open(filename) as fd:
		lines = fd.readlines()

		lines = list(map(lambda xx: list(map(float, xx.strip().split())), lines))
		return np.array(lines)

feature_names = "m,n,nnz,maxRow,minRow,avgRow,maxCol,minCol,avgCol".split(",")

def print_info(estimator):
	# print(estimator.get_params())
	print(estimator.feature_importances_)
	print(estimator.max_features_)
	print(estimator.n_features_)
	print(estimator.tree_)
	n_nodes = estimator.tree_.node_count
	children_left = estimator.tree_.children_left
	children_right = estimator.tree_.children_right
	feature = estimator.tree_.feature
	threshold = estimator.tree_.threshold


	# The tree structure can be traversed to compute various properties such
	# as the depth of each node and whether or not it is a leaf.
	node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
	is_leaves = np.zeros(shape=n_nodes, dtype=bool)
	stack = [(0, -1)]  # seed is the root node id and its parent depth
	while len(stack) > 0:
		node_id, parent_depth = stack.pop()
		node_depth[node_id] = parent_depth + 1

		# If we have a test node
		if (children_left[node_id] != children_right[node_id]):
			stack.append((children_left[node_id], parent_depth + 1))
			stack.append((children_right[node_id], parent_depth + 1))
		else:
			is_leaves[node_id] = True

	print("The binary tree structure has %s nodes and has "
		  "the following tree structure:"
		  % n_nodes)
	for i in range(n_nodes):
		if is_leaves[i]:
			print("%snode=%s leaf node." % (node_depth[i] * "\t", i))
		else:
			print("%snode=%s test node: go to node %s if `%s` <= %s else to "
			# print("%snode=%s test node: go to node %s if X[:, %s] <= %s else to "
				  "node %s."
				  % (node_depth[i] * "\t",
					 i,
					 children_left[i],
					 feature_names[feature[i]],
					 threshold[i],
					 children_right[i],
					 ))
	print()
datas = load_data("testdata.txt")
# print(datas.shape)
# print(datas)
X = datas[:,:9]
alpha = datas[:,9]
beta = datas[:,10]
# X, alpha, beta = shuffle(X, alpha, beta, random_state=1)
test_X, test_alpha, test_beta = shuffle(X[-2:], alpha[-2:], beta[-2:])

clf = tree.DecisionTreeRegressor(max_depth=4)
# 针对alpha
alpha_clf = clf.fit(X, alpha)
a_score = alpha_clf.score(test_X, test_alpha)
print("alpha score:{}".format(a_score))
print_info(alpha_clf)
# 从结果中可以看出，对于alpha这个值
## 针对beta
beta_clf = clf.fit(X, beta)
b_score = beta_clf.score(test_X, test_beta)
print("beta score:{}".format(b_score))
print_info(beta_clf)

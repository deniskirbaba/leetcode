# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def form_seq(self, node, seq):
#         if node.left or node.right:
#             if node.left:
#                 self.form_seq(node.left, seq)
#             if node.right:
#                 self.form_seq(node.right, seq)
#         else:
#             seq.append(node.val)


#     def leafSimilar(self, root1: TreeNode | None = None, root2: TreeNode | None = None) -> bool:
#         tree1_seq = []
#         tree2_seq = []
#         self.form_seq(root1, tree1_seq)
#         self.form_seq(root2, tree2_seq)
#         print(tree1_seq, tree2_seq)

#         if len(tree1_seq) != len(tree2_seq):
#             return False
#         else:
#             for i in range(len(tree1_seq)):
#                 if tree1_seq[i] != tree2_seq[i]:
#                     return False
#             return True
        


# class Solution:
#     def leafSimilar(self, root1, root2):
#         def dfs(node):
#             if node:
#                 if not node.left and not node.right:
#                     yield node.val
#                 yield from dfs(node.left)
#                 yield from dfs(node.right)

#         return list(dfs(root1)) == list(dfs(root2))


import itertools
class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if not node: return
            if not node.left and not node.right: yield node.val
            for i in dfs(node.left): yield i
            for i in dfs(node.right): yield i
        return all(a == b for a, b in itertools.zip_longest(dfs(root1), dfs(root2)))
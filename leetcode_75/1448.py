# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def __init__(self):
        self.good_nodes = 0

    def calculate_good_nodes(self, node: TreeNode, max_val: int) -> None:
        if node.val >= max_val:
            self.good_nodes += 1
        max_val = max(max_val, node.val)
        if node.left:
            self.calculate_good_nodes(node.left, max_val)
        if node.right:
            self.calculate_good_nodes(node.right, max_val)

    def goodNodes(self, root: TreeNode) -> int:
        self.calculate_good_nodes(root, -10e4)
        return self.good_nodes
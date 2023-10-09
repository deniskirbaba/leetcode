# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     max_depth = 0

#     def inspect_node(self, node: TreeNode, depth: int) -> None:
#         if node.left:
#             self.inspect_node(node.left, depth + 1)
#         if node.right:
#             self.inspect_node(node.right, depth + 1)
#         self.max_depth = max(self.max_depth, depth)


#     def maxDepth(self, root: TreeNode | None = None) -> int:
#         if not root:
#             return 0
#         self.inspect_node(root, 1)
#         return self.max_depth


class Solution:
    def maxDepth(self, root: TreeNode | None = None) -> int:
        if not root:
            return 0
        max_left_depth = self.maxDepth(root.left)
        max_right_depth = self.maxDepth(root.right)
        return max(max_left_depth, max_right_depth) + 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs solution
# class Solution:
#     def longestZigZag(self, root: TreeNode | None) -> int:
#         self.longest_path = 0
#         def dfs(node: TreeNode, prev_side: str = None, cur_length: int = 0):
#             if not node:
#                 self.longest_path = max(self.longest_path, cur_length)
#                 return
            
#             left_cur_length, right_cur_length = 0, 0
#             if prev_side == 'l':
#                 left_cur_length = cur_length + 1
#             elif prev_side == 'r':
#                 right_cur_length = cur_length + 1

#             dfs(node.left, 'r', left_cur_length)
#             dfs(node.right, 'l', right_cur_length)
#         dfs(root)
#         return self.longest_path



# bfs solution
from collections import deque

class Solution():
    def longestZigZag(self, root: TreeNode | None) -> int:
        self.longest_path = 0
        queue = deque([(root, None, 0)])

        while queue:
            left_length, right_length = 1, 1
            node, side, length = queue.pop()
            if node.left:
                if side == 'l':
                    left_length = length + 1
                queue.appendleft((node.left, 'r', left_length))
            if node.right:
                if side == 'r':
                    right_length = length + 1
                queue.appendleft((node.right, 'l', right_length))
            self.longest_path = max(self.longest_path, length)

        return self.longest_path

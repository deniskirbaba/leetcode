# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.paths = 0
        self.sum_paths_data = {0: 1}

    def calc_paths(self, node: TreeNode, target_sum: int, cur_sum: int):
        if not node:
            return
        cur_sum += node.val
        residual_sum = cur_sum - target_sum
        self.paths += self.sum_paths_data.get(residual_sum, 0)
        self.sum_paths_data[cur_sum] = self.sum_paths_data.get(cur_sum, 0) + 1

        self.calc_paths(node.left, target_sum, cur_sum)
        self.calc_paths(node.right, target_sum, cur_sum)
        self.sum_paths_data[cur_sum] -= 1

    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        self.calc_paths(root, targetSum, 0)
        return self.paths

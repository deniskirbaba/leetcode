class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        left, right = 0, length - 1
        area = 0
        while left < right:
            h_left, h_right = height[left], height[right]
            area = max(area, (right - left) * min(h_left, h_right))
            if h_left < h_right:
                left += 1
            else:
                right -= 1
        return area
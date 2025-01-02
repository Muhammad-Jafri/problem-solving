from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left_ptr = 0
        right_ptr = len(height) - 1
        max_area = 0

        while (left_ptr < right_ptr):

            max_area = max(max_area, min(
                height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr))

            if height[left_ptr] <= height[right_ptr]:

                left_ptr += 1

            else:

                right_ptr -= 1

        return max_area


sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height=height))

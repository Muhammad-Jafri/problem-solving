from typing import List


class Solution:
    def lengthOfLIS(
        self, nums: List[int]
    ) -> int:  # Works but shitty performance, could do better with dp (not the one you are thinking of)
        res = 0

        def check_if_increasing(arr):
            # Iterate through the array
            for i in range(len(arr) - 1):
                # Check if the current element is not less than the next element
                if arr[i] >= arr[i + 1]:
                    return False  # Not strictly increasing
            return True  # All elements are strictly increasing

        def dfs(idx, sub_arr):
            nonlocal res
            if idx >= len(nums):
                if check_if_increasing(sub_arr):
                    print(sub_arr)
                    res = max(res, len(sub_arr))
                return

            dfs(idx + 1, sub_arr + [nums[idx]])
            dfs(idx + 1, sub_arr)

        dfs(0, [])
        return res


n = [10, 20, 35, 80]
print(Solution().lengthOfLIS(nums=n))

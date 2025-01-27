from typing import List


class Solution:
    # Go with a fucking brute force solution at this point FIXME optimize it later lil bro
    def minOperations(self, boxes: str) -> List[int]:

        boxes = list(boxes)
        n = len(boxes)
        left = [0] * n
        right = [0] * n
        res = [0] * n

        for i in range(n):

            for j in range(i + 1, n):

                if boxes[j] == "1":

                    left[i] += j - i

        for i in range(n - 1, -1, -1):

            for j in range(i - 1, -1, -1):

                if boxes[j] == "1":

                    left[i] += i - j

        for i in range(n):

            res[i] = left[i] + right[i]

        return res


boxes = "110"
sol = Solution()
print(sol.minOperations(boxes=boxes))

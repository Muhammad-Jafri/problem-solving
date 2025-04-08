from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = []

        for i in range(n):
            # Create a hashmap for values of A[0:i+1]
            hashmap = {}
            for j in range(i + 1):  # Iterate over A[0:i+1]
                hashmap[A[j]] = hashmap.get(A[j], 0) + 1

            # Optional: For debugging, print the hashmap for each prefix
            print(f"Hashmap for A[0:{i + 1}]: {hashmap}")

            # Count the common elements in current prefix of A and B
            temp = 0
            for j in range(i + 1):  # Check only up to i in B
                if B[j] in hashmap:
                    temp += 1

            # Append the result for the current prefix
            res.append(temp)

        return res

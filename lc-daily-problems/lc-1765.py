from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        no_rows = len(isWater)
        no_cols = len(isWater[0])
        res = [[0 for i in range(no_cols)] for j in range(no_rows)]

        

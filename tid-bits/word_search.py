from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtrack(row, col, idx):
            # Boundary conditions
            if (
                row < 0
                or row >= m
                or col < 0
                or col >= n
                or board[row][col] != word[idx]
            ):
                return False

            # Success condition: if we've matched the entire word
            if idx == len(word) - 1:
                return True

            # Temporarily mark the current cell as visited
            temp = board[row][col]
            board[row][col] = "#"

            # Explore the 4 directions
            found = (
                backtrack(row - 1, col, idx + 1)
                or backtrack(row + 1, col, idx + 1)
                or backtrack(row, col - 1, idx + 1)
                or backtrack(row, col + 1, idx + 1)
            )

            # Restore the cell's original value
            board[row][col] = temp

            return found

        # Start backtracking from each cell
        for i in range(m):
            for j in range(n):
                if (
                    board[i][j] == word[0]
                ):  # Only start backtracking if the first letter matches
                    if backtrack(i, j, 0):
                        return True

        return False


# Test the solution
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(Solution().exist(board=board, word=word))  # Output: True

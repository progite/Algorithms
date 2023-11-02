class Solution:
    def find(self, i, j, grid, dp):
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]
        if i >= len(grid) or j >= len(grid[0]):
            return float("inf")
        if (i, j) in dp:
            return dp[(i, j)]
        dp[(i, j)] = grid[i][j] + min(self.find(i + 1, j, grid, dp), self.find(i, j + 1, grid, dp))
        return dp[(i, j)]

    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.find(0, 0, grid, {})
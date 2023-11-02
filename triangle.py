class Solution:
    def find(self, i, j, triangle, dp):
        if i >= len(triangle):
            return 0
        if (i, j) in dp:
            return dp[(i, j)]
        dp[(i, j)] = triangle[i][j] + min(self.find(i + 1, j, triangle, dp), self.find(i + 1, j + 1, triangle, dp))
        return dp[(i, j)]

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        return self.find(0, 0, triangle, {})
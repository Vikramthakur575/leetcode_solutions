class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        length = m + n - 1

        if length % 2 == 1:
            return False

        if grid[0][0] == ')':
            return False

        # dp[i][j][balance]
        dp = [[[False] * (length + 1) for _ in range(n)] 
              for _ in range(m)]

        dp[0][0][1] = True

        for i in range(m):
            for j in range(n):
                for balance in range(length + 1):

                    if not dp[i][j][balance]:
                        continue

                    # Move down
                    if i + 1 < m:
                        new_balance = balance + (
                            1 if grid[i + 1][j] == '(' else -1
                        )

                        if new_balance >= 0:
                            dp[i + 1][j][new_balance] = True

                    # Move right
                    if j + 1 < n:
                        new_balance = balance + (
                            1 if grid[i][j + 1] == '(' else -1
                        )

                        if new_balance >= 0:
                            dp[i][j + 1][new_balance] = True

        return dp[m - 1][n - 1][0]
        
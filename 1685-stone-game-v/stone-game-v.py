import bisect
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        doubled = [2 * p for p in prefix]  # monotonic, avoids fractions

        NEG = float('-inf')
        dp = [[0] * n for _ in range(n)]
        # maxLeft[i][k] = max_{k'=i}^{k} (dp[i][k'] + sum(i,k'))
        maxLeft = [[NEG] * n for _ in range(n)]
        # maxRight[j][m] = max_{m'=m}^{j} (dp[m'][j] + sum(m',j))
        maxRight = [[NEG] * (n + 1) for _ in range(n)]

        for i in range(n):
            maxLeft[i][i] = stoneValue[i]      # dp[i][i] = 0
            maxRight[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                total = prefix[j + 1] - prefix[i]
                best = NEG

                # ---- left-kept: largest k in [i, j-1] with 2*sum(i,k) <= total ----
                target = 2 * prefix[i] + total
                idx = bisect.bisect_right(doubled, target, i + 1, j + 1) - 1
                if idx >= i + 1:
                    k = idx - 1
                    if maxLeft[i][k] != NEG:
                        best = max(best, maxLeft[i][k])

                # ---- right-kept: smallest k in [i, j-1] with 2*sum(k+1,j) <= total ----
                target2 = 2 * prefix[j + 1] - total
                idx2 = bisect.bisect_left(doubled, target2, i + 1, j + 1)
                if idx2 <= j:
                    if maxRight[j][idx2] != NEG:
                        best = max(best, maxRight[j][idx2])

                dp[i][j] = best if best != NEG else 0

                maxLeft[i][j] = max(maxLeft[i][j - 1], dp[i][j] + total)
                maxRight[j][i] = max(maxRight[j][i + 1], dp[i][j] + total)

        return dp[0][n - 1]
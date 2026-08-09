class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = sum of piles from i to end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, m) = maximum stones current player can get
        # starting from index i with M = m
        memo = {}

        def dp(i, m):

            # Can take all remaining piles
            if i + 2 * m >= n:
                return suffix[i]

            if (i, m) in memo:
                return memo[(i, m)]

            best = 0

            # Try taking x piles
            for x in range(1, 2 * m + 1):

                next_i = i + x
                next_m = max(m, x)

                # Total remaining stones minus what opponent
                # can get.
                current = suffix[i] - dp(next_i, next_m)

                best = max(best, current)

            memo[(i, m)] = best

            return best

        return dp(0, 1)
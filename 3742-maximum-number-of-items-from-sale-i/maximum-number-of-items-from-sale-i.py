from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        # Calculate value of each item
        values = [1] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    values[i] += 1

        # Group items by price
        groups = {}

        for i in range(n):
            price = items[i][1]
            groups.setdefault(price, []).append(values[i])

        dp = [-1] * (budget + 1)
        dp[0] = 0

        ans = 0

        # Process prices in descending order
        for price in sorted(groups.keys(), reverse=True):

            current = [-1] * (budget + 1)

            for value in groups[price]:

                for c in range(budget, price - 1, -1):

                    if current[c - price] != -1:
                        current[c] = max(
                            current[c],
                            current[c - price] + value
                        )

                    if dp[c - price] != -1:
                        current[c] = max(
                            current[c],
                            dp[c - price] + value
                        )

            # Calculate total including extra copies
            for c in range(price, budget + 1):
                if current[c] != -1:
                    extra = (budget - c) // price
                    ans = max(ans, current[c] + extra)

            # Update DP
            for c in range(budget + 1):
                dp[c] = max(dp[c], current[c])

        return ans
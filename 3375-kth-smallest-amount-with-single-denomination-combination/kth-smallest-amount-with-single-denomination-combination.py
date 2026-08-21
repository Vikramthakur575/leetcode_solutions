class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        from math import gcd

        n = len(coins)

        # Count how many valid amounts are <= x
        def count(x):
            ans = 0

            for mask in range(1, 1 << n):

                lcm = 1
                bits = 0
                valid = True

                for i in range(n):

                    if mask & (1 << i):

                        bits += 1

                        g = gcd(lcm, coins[i])
                        lcm = lcm // g * coins[i]

                        if lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                value = x // lcm

                if bits % 2 == 1:
                    ans += value
                else:
                    ans -= value

            return ans

        # Binary search
        left = 1
        right = min(coins) * k

        while left < right:

            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
        
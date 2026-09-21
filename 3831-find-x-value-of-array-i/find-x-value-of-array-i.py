class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k

        # dp[r] = number of subarrays ending at the
        # previous position with product % k == r
        dp = [0] * k

        for num in nums:
            rem = num % k

            new_dp = [0] * k

            # Start a new subarray [num]
            new_dp[rem] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_rem = (r * rem) % k
                    new_dp[new_rem] += dp[r]

            # Every subarray ending here contributes
            # to the final answer
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans
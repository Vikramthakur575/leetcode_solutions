
from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = float('inf')

        for i in range(n):
            for j in range(i + l, min(i + r, n) + 1):

                curr_sum = prefix[j] - prefix[i]

                if curr_sum > 0:
                    ans = min(ans, curr_sum)

        return ans if ans != float('inf') else -1

        
from typing import List
from collections import Counter

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                expected = target[start:start + k]

                if Counter(block) != Counter(expected):
                    valid = False
                    break

                descents = sum(
                    block[i] > block[(i + 1) % k]
                    for i in range(k)
                )

                if descents > 1:
                    valid = False
                    break

            if valid:
                ans += k

        return ans
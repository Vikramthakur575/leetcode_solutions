
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(
        self, nums: List[int], k: int
    ) -> int:

        nums = nums[::-1]
        n = len(nums)

        # [maximum value, count, sum of original values]
        dq = deque()

        left = 0
        cost = 0
        ans = 0

        for right in range(n):
            x = nums[right]

            count = 1
            total = x

            # Merge groups whose maximum is <= x
            while dq and dq[-1][0] <= x:
                value, cnt, group_sum = dq.pop()

                cost += (x - value) * cnt

                count += cnt
                total += group_sum

            dq.append([x, count, total])

            # Shrink window until its cost is valid
            while cost > k:
                value = dq[0][0]

                cost -= value - nums[left]

                dq[0][1] -= 1
                dq[0][2] -= nums[left]

                if dq[0][1] == 0:
                    dq.popleft()

                left += 1

            # Every subarray ending at right
            # and starting between left and right is valid
            ans += right - left + 1

        return ans

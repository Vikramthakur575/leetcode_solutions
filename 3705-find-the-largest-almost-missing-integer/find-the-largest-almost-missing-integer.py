class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        count = {}

        # Check every subarray of size k
        for i in range(len(nums) - k + 1):

            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            # Each number in this window appears
            # in exactly one subarray occurrence
            for x in seen:
                count[x] = count.get(x, 0) + 1

        ans = -1

        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans
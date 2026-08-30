class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n = len(nums)

        min_idx = 0
        max_idx = 0

        for i in range(n):
            if nums[i] < nums[min_idx]:
                min_idx = i

            if nums[i] > nums[max_idx]:
                max_idx = i

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Both from front
        front = right + 1

        # Both from back
        back = n - left

        # One from front, one from back
        both = left + 1 + n - right

        return min(front, back, both)
        

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        index = {value: i for i, value in enumerate(nums)}
        swaps = 0

        for i in range(len(nums)):
            if nums[i] == arr[i]:
                continue

            j = index[arr[i]]

            index[nums[i]] = j
            index[arr[i]] = i

            nums[i], nums[j] = nums[j], nums[i]
            swaps += 1

        return swaps

        
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n = len(nums)

        # Store (value, original_index)
        arr = sorted((nums[i], i) for i in range(n))

        ans = [0] * n

        start = 0

        while start < n:

            end = start

            # Find one connected group
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Indices belonging to this group
            indices = []

            for i in range(start, end + 1):
                indices.append(arr[i][1])

            # Values are already sorted
            values = []

            for i in range(start, end + 1):
                values.append(arr[i][0])

            # Put smallest values at smallest indices
            indices.sort()

            for i in range(len(indices)):
                ans[indices[i]] = values[i]

            start = end + 1

        return ans
        
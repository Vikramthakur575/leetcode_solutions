class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = n + 1

        # best[i] = shortest target-sum subarray
        # completely within arr[0...i]
        best = [INF] * n

        left = 0
        curr_sum = 0
        answer = INF

        for right in range(n):
            curr_sum += arr[right]

            # Since all numbers are positive,
            # shrink window while sum is too large.
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # Found a subarray with sum = target
            if curr_sum == target:
                length = right - left + 1

                # Check if there is a previous
                # non-overlapping target subarray.
                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, length + best[left - 1])

                # This is the best target subarray
                # ending at or before 'right'.
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)

            else:
                # No new target subarray ending here.
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if answer == INF else answer
        
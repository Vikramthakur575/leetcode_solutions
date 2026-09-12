from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: [left, right, weight, original_index]
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by left endpoint
        arr.sort()

        starts = [x[0] for x in arr]

        # dp[k][i] =
        # best (score, indices) using intervals from i onward,
        # choosing at most k intervals.
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(n - 1, -1, -1):
                l, r, w, original_index = arr[i]

                # Option 1: skip this interval
                skip_score, skip_indices = dp[k][i + 1]

                # Find first interval whose left > r
                next_i = bisect_right(starts, r)

                # Option 2: take this interval
                next_score, next_indices = dp[k - 1][next_i]

                take_score = w + next_score
                take_indices = tuple(
                    sorted((original_index,) + next_indices)
                )

                # Choose better score.
                # If scores are equal, choose lexicographically smaller indices.
                if take_score > skip_score:
                    dp[k][i] = (take_score, take_indices)
                elif take_score < skip_score:
                    dp[k][i] = (skip_score, skip_indices)
                else:
                    dp[k][i] = min(
                        (take_score, take_indices),
                        (skip_score, skip_indices)
                    )

        return list(dp[4][0][1])
        
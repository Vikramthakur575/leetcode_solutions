class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        # Segment tree arrays
        size = 4 * n
        total = [0] * size       # sum of values
        squares = [0] * size     # sum of squares
        lazy = [0] * size        # pending addition

        def apply(node, l, r, val):
            length = r - l + 1

            # (x + val)^2 = x^2 + 2*x*val + val^2
            squares[node] = (
                squares[node]
                + 2 * val * total[node]
                + length * val * val
            )

            total[node] += length * val
            lazy[node] += val

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            val = lazy[node]

            apply(node * 2, l, mid, val)
            apply(node * 2 + 1, mid + 1, r, val)

            lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return

            push(node, l, r)

            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)

            total[node] = total[node * 2] + total[node * 2 + 1]
            squares[node] = squares[node * 2] + squares[node * 2 + 1]

        last = {}
        ans = 0

        for r, x in enumerate(nums):
            # Previous occurrence of x.
            # If none, no left endpoint is excluded.
            p = last.get(x, -1)

            # For every l in [p+1, r], x becomes a new
            # distinct element of nums[l..r].
            update(1, 0, n - 1, p + 1, r)

            # Root contains all subarrays ending at r.
            ans = (ans + squares[1]) % MOD

            last[x] = r

        return ans
        
class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)

        # Each node:
        # [left_char, right_char, left_len, right_len, best, length]
        tree = [None] * (4 * n)

        def merge(a, b):

            if a is None:
                return b

            if b is None:
                return a

            lc1, rc1, ll1, rl1, best1, len1 = a
            lc2, rc2, ll2, rl2, best2, len2 = b

            left_char = lc1
            right_char = rc2

            left_len = ll1
            right_len = rl2

            best = max(best1, best2)

            # The boundary characters are equal,
            # so the two groups can be joined.
            if rc1 == lc2:

                combined = rl1 + ll2

                best = max(best, combined)

                # Entire left segment has one repeating character
                if ll1 == len1:
                    left_len = len1 + ll2

                # Entire right segment has one repeating character
                if rl2 == len2:
                    right_len = len2 + rl1

            return (
                left_char,
                right_char,
                left_len,
                right_len,
                best,
                len1 + len2
            )

        def build(node, start, end):

            if start == end:
                tree[node] = (
                    s[start],
                    s[start],
                    1,
                    1,
                    1,
                    1
                )
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, start, end, idx, ch):

            if start == end:
                tree[node] = (
                    ch,
                    ch,
                    1,
                    1,
                    1,
                    1
                )
                return

            mid = (start + end) // 2

            if idx <= mid:
                update(node * 2, start, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, end, idx, ch)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # Build initial tree
        build(1, 0, n - 1)

        answer = []

        for ch, idx in zip(queryCharacters, queryIndices):

            update(1, 0, n - 1, idx, ch)

            # tree[1][4] is the longest repeating substring
            answer.append(tree[1][4])

        return answer
        
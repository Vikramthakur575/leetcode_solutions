class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Build the smallest valid interval for each character
        for c in range(26):
            if last[c] == -1:
                continue

            left = first[c]
            right = last[c]

            i = left
            valid = True

            while i <= right:
                x = ord(s[i]) - ord('a')

                # This character has an occurrence
                # before our starting point.
                if first[x] < left:
                    valid = False
                    break

                # We must include all occurrences of x.
                right = max(right, last[x])

                i += 1

            if valid:
                intervals.append((left, right))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result
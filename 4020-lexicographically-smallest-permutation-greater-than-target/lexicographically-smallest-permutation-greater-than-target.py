class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        n = len(s)

        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        ans = []

        for i in range(n):

            x = ord(target[i]) - 97

            # Try to keep the prefix equal to target
            if cnt[x] > 0:
                cnt[x] -= 1
                ans.append(target[i])
                continue

            # We cannot continue equal.
            # Try making the current character greater.
            for c in range(x + 1, 26):

                if cnt[c] > 0:

                    ans.append(chr(c + 97))
                    cnt[c] -= 1

                    # Smallest possible suffix
                    for d in range(26):
                        while cnt[d] > 0:
                            ans.append(chr(d + 97))
                            cnt[d] -= 1

                    return ''.join(ans)

            # No greater character here.
            # We must backtrack.
            break

        # Backtrack through the matching prefix
        for i in range(len(ans) - 1, -1, -1):

            # Return this character to available characters
            old = ord(ans[i]) - 97
            cnt[old] += 1

            target_char = ord(target[i]) - 97

            # Find smallest character > target[i]
            for c in range(target_char + 1, 26):

                if cnt[c] > 0:

                    result = ans[:i]
                    result.append(chr(c + 97))
                    cnt[c] -= 1

                    # Fill suffix in ascending order
                    for d in range(26):
                        result.extend(chr(d + 97) for _ in range(cnt[d]))

                    return ''.join(result)

        return ""
        
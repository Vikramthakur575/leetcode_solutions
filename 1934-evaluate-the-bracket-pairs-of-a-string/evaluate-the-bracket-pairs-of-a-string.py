class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Store key-value pairs in a dictionary
        mp = {key: value for key, value in knowledge}

        ans = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = i + 1

                # Find closing bracket
                while s[j] != ')':
                    j += 1

                # Extract key
                key = s[i + 1:j]

                # Replace with value, or '?' if unknown
                ans.append(mp.get(key, '?'))

                # Move after ')'
                i = j + 1

            else:
                ans.append(s[i])
                i += 1

        return ''.join(ans)
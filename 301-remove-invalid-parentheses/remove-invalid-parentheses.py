class Solution:
    def removeInvalidParentheses(self, s: str):
        left_remove = 0
        right_remove = 0

        # Find minimum number of '(' and ')' to remove
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def dfs(index, path, balance, left_remove, right_remove):
            # Reached the end
            if index == len(s):
                if balance == 0 and left_remove == 0 and right_remove == 0:
                    result.add("".join(path))
                return

            ch = s[index]

            # Normal character
            if ch != '(' and ch != ')':
                path.append(ch)
                dfs(index + 1, path, balance, left_remove, right_remove)
                path.pop()
                return

            # Option 1: remove current parenthesis
            if ch == '(' and left_remove > 0:
                dfs(index + 1, path, balance, left_remove - 1, right_remove)

            if ch == ')' and right_remove > 0:
                dfs(index + 1, path, balance, left_remove, right_remove - 1)

            # Option 2: keep current parenthesis
            if ch == '(':
                path.append(ch)
                dfs(index + 1, path, balance + 1, left_remove, right_remove)
                path.pop()

            else:
                # Can't keep ')' if there is no '(' available to match it
                if balance > 0:
                    path.append(ch)
                    dfs(index + 1, path, balance - 1, left_remove, right_remove)
                    path.pop()

        dfs(0, [], 0, left_remove, right_remove)

        return list(result)
        

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # New parent array
        new_parent = parent[:]

        # Track the closest ancestor for each character
        last = [-1] * 26

        def dfs(node):
            char = ord(s[node]) - ord('a')

            # Save previous ancestor with the same character
            old = last[char]

            # Update parent if matching ancestor exists
            if old != -1:
                new_parent[node] = old

            last[char] = node

            # Visit original children
            for child in children[node]:
                dfs(child)

            # Backtrack
            last[char] = old

        dfs(0)

        # Build the modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Calculate subtree sizes
        answer = [1] * n

        def calculate(node):
            for child in new_children[node]:
                calculate(child)
                answer[node] += answer[child]

        calculate(0)

        return answer

        
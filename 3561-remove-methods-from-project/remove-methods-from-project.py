from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        suspicious = [False] * n

        q = deque([k])
        suspicious[k] = True

        while q:
            node = q.popleft()

            for nei in graph[node]:
                if not suspicious[nei]:
                    suspicious[nei] = True
                    q.append(nei)

        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        ans = []

        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans
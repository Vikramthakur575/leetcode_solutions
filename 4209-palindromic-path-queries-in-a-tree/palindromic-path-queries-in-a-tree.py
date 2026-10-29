
class Solution:
    def palindromePath(self, n, edges, s, queries):
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        root_xor = [0] * n
        timer = 0

        chars = list(s)
        masks = [1 << (ord(c) - ord('a')) for c in chars]

        # Iterative DFS: Euler Tour, LCA parents, root path XOR
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = u if p == -1 else p
                root_xor[u] = masks[u] ^ (
                    root_xor[p] if p != -1 else 0
                )

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        for k in range(1, LOG):
            for u in range(n):
                parent[k][u] = parent[k - 1][parent[k - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        # Fenwick Tree for subtree range-XOR updates
        bit = [0] * (n + 2)

        def add(i, value):
            i += 1
            while i <= n + 1:
                bit[i] ^= value
                i += i & -i

        def point_query(i):
            result = 0
            i += 1
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                new_mask = 1 << (ord(c) - ord('a'))
                delta = masks[u] ^ new_mask

                # Update root-path XOR for every node in u's subtree
                add(tin[u], delta)
                add(tout[u], delta)

                masks[u] = new_mask
                chars[u] = c

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                # Current root-to-node XOR masks
                xu = root_xor[u] ^ point_query(tin[u])
                xv = root_xor[v] ^ point_query(tin[v])

                # XOR of characters along the inclusive path
                path_mask = xu ^ xv ^ masks[w]

                ans.append((path_mask & (path_mask - 1)) == 0)

        return ans

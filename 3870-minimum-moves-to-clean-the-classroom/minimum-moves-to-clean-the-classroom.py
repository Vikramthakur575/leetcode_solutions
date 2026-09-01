from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        # Find start and assign an index to every litter cell
        litter = {}
        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        k = len(litter)

        # No litter to collect
        if k == 0:
            return 0

        target = (1 << k) - 1

        # State: (r, c, mask, remaining_energy)
        q = deque()
        q.append((start[0], start[1], 0, energy))

        # Visited states
        visited = set()
        visited.add((start[0], start[1], 0, energy))

        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                # All litter collected
                if mask == target:
                    return moves

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Outside grid
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # Need 1 energy for every move
                    if e == 0:
                        continue

                    new_energy = e - 1
                    new_mask = mask

                    # Collect litter
                    if (nr, nc) in litter:
                        idx = litter[(nr, nc)]
                        new_mask |= (1 << idx)

                    # Reset energy on R
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (nr, nc, new_mask, new_energy)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            moves += 1

        return -1
        
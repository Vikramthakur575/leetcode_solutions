import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            # Release servers that have completed their requests
            while busy and busy[0][0] <= arrival[i]:
                end_time, server = heapq.heappop(busy)
                available.add(server)

            # If all servers are busy, drop the request
            if not available:
                continue

            # Find the first available server >= i % k
            idx = available.bisect_left(i % k)

            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            # Assign request
            count[server] += 1

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        # Find the maximum number of requests handled
        max_count = max(count)

        return [i for i in range(k) if count[i] == max_count]
        
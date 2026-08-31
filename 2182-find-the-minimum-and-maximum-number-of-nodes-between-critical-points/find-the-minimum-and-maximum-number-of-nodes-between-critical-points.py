class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> List[int]:

        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:

            # Local maximum or local minimum
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - last)

                last = index

            prev = curr
            curr = curr.next
            index += 1

        # Fewer than 2 critical points
        if first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]
        
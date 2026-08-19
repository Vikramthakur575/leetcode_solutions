class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}
        for r,s in reservedSeats:
            rows[r]=rows.get(r,0) | (1<<s)
        ans = 2 * n

        for mask in rows.values():
            ans-=2
            left = (mask & 0b000000111100) == 0

            # seats 6-9
            right = (mask & 0b001111000000) == 0

            # seats 4-7
            middle = (mask & 0b000011110000) == 0

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans


        
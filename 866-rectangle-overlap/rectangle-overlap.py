
class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1 = max(rec1[0], rec2[0])
        y1 = max(rec1[1], rec2[1])

        x2 = min(rec1[2], rec2[2])
        y2 = min(rec1[3], rec2[3])

        width = x2 - x1
        height = y2 - y1

        return width > 0 and height > 0
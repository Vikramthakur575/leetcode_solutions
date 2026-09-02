class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even=0
        odd=0
        for x in nums1:
            if x%2 == 0:
                even+=1
            else:
                odd+=1
        if even == len(nums1)or odd == len(nums1):
            return True
        return True

        
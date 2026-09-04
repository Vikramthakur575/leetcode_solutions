from typing import List

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:  # <-- renamed here
        n = len(nums)
        
        prefixMax = [0] * n
        prefixMax[0] = nums[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i-1], nums[i])
        
        suffixMin = [0] * n
        suffixMin[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffixMin[i] = min(suffixMin[i+1], nums[i])
        
        for i in range(n):
            instability = prefixMax[i] - suffixMin[i]
            if instability <= k:
                return i
        
        return -1

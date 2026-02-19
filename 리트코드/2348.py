# 2348. Number of Zero-Filled Subarrays
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        run = 0
        for x in nums:
            if x == 0:
                run += 1
                total += run
            else:
                run = 0
        return total
        

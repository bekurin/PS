class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        deduplicated_nums = set(nums)
        return len(deduplicated_nums) != len(nums)
        

# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_sorted_nums = sorted(list(set(nums)))
        k = len(unique_sorted_nums)
        
        nums[:k] = unique_sorted_nums
        return k

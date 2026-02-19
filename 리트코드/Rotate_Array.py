# Rotate Array
class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    if not nums:
        return

    k %= len(nums)

    if k == 0:
        return
    nums[:] = nums[-k:] + nums[:-k]

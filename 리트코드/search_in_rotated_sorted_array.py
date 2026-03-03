from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 왼쪽 절반이 정렬된 경우
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:  # target이 왼쪽 범위 안에 있음
                    right = mid - 1
                else:                                  # target이 오른쪽에 있음
                    left = mid + 1

            # 오른쪽 절반이 정렬된 경우
            else:
                if nums[mid] < target <= nums[right]:  # target이 오른쪽 범위 안에 있음
                    left = mid + 1
                else:                                   # target이 왼쪽에 있음
                    right = mid - 1

        return -1

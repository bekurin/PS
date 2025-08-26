# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        i, j = 0, len(height) - 1

        while i < j:
            w = j - i
            h = min(height[i], height[j])
            answer = max(answer, h * w)

            if (height[i] >= height[j]):
                j -= 1
            else:
                i += 1
        return answer

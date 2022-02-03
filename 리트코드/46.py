# 리트코드 No.46 Permutations
class Solution:
    def permute(self, nums: list) -> list:
        answer = []
        prev_elements = []
        
        def dfs(elements):
            if len(elements) == 0:
              answer.append(prev_elements[:])
            
            for element in elements:
                next_elements = elements[:]
                next_elements.remove(element)

                prev_elements.append(element)
                dfs(next_elements)
                prev_elements.pop()
        dfs(nums)
        return answer

solution = Solution()
print(solution.permute([1,2,3,4]))
# 리트코드 No.17 Letter Combinations of a Phone Number 
"""
백트레킹
모든 문자에 대하여 문자 단위로 재귀 탐색을 실시한다.
"""
class Solution:
    def letterCombinations(self, digits: str) -> list:
        answer = []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def dfs(index, path):
            if len(path) == len(digits):
                answer.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    print(i, path + j)
                    dfs(i + 1, path + j)
                    
        if not digits:
            return []
        dfs(0, "")
        return answer

solution = Solution()
print(solution.letterCombinations("234"))
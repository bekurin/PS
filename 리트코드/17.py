"""
백트레킹
모든 문자에 대하여 문자 단위로 재귀 탐색을 실시한다. 
1. digits의 값 자릿수 단위 반복
2. digit에 해당하는 모든 문자열 반복
3. dfs(index, path)를 재귀 호출
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
"""
한번 더 풀어서
"""

import itertools

class Solution:
    _digit_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = [list(self._digit_to_letters[d]) for d in digits]

        combinations = [''.join(p) for p in itertools.product(*letters)]
        return combinations

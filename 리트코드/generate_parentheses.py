from typing import List

"""
[문제 요약] n개의 괄호 쌍으로 만들 수 있는 모든 유효한 조합 생성
[알고리즘] 백트래킹 (Backtracking)
[핵심 규칙]
    1. '(' 개수는 n을 초과할 수 없다. (open < n)
    2. ')' 개수는 현재 사용된 '(' 개수보다 작을 때만 추가 가능하다. (close < open)
    3. 문자열 길이가 2*n에 도달하면 결과 리스트에 추가한다.
[시간 복잡도] O(4^n / sqrt(n)) - 카탈란 수(Catalan Number)에 비례
"""
class Solution:
    def __init__(self):
        self.n = 0
        self.result = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self._backtrack("", 0, 0)
        return self.result

    def _backtrack(self, current, open_count, close_count):
        if len(current) == 2 * self.n:
            self.result.append(current)
            return

        if open_count < self.n:
            self._backtrack(current + "(", open_count + 1, close_count)

        if close_count < open_count:
            self._backtrack(current + ")", open_count, close_count + 1)


if "__main__" == __name__:
    solution = Solution()
    print(solution.generateParenthesis(3))

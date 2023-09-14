# 프로그래머스 No.43105 정수 삼각형


def solution(triangle):
  dp = [[0 for _ in i] for i in triangle]
  dp[0][0] = triangle[0][0]

  for i in range(len(triangle)):
    for j in range(i):
      dp[i][j] = max(dp[i][j], dp[i - 1][j] + triangle[i][j])
      dp[i][j + 1] = dp[i - 1][j] + triangle[i][j + 1]
  return max(dp[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))

# 프로그래머스 no.42842 카펫
def solution(brown, yellow):
  answer = []
  ab = brown + yellow

  for a in range(3, ab // 2 + 1):
    if ab % a == 0 and ab // a <= a:
      b = ab // a
      if (a-2) * (b-2) == yellow:
        answer.append([a, b])
  return answer[0]

brown = 18
yellow = 6
print(solution(brown, yellow))
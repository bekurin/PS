# 프로그래머스 No.181188 요격 시스템
def solution(targets):
  answer = 0
  missile = 0
  for s, e in sorted(targets):
    if missile > s:
      missile = min(missile, e)
    else:
      missile = e
      answer += 1
  return answer


targets = [[[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]],
           [[1, 10]], [[1, 10], [1, 9], [1, 8], [1, 7]],
           [[3, 6], [2, 4], [5, 6], [1, 3]], [[1, 1]]]

for target in targets:
  print(solution(target))

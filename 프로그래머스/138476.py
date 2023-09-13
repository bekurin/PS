# 프로그래머스 No.138476 귤 고르기
from collections import Counter


def solution(k, tangerine):
  answer, tangerine_sum = 0, 0
  tangerine_counter = Counter(tangerine).most_common()

  for counter in tangerine_counter:
    item, count = counter
    answer += 1
    tangerine_sum += count
    if tangerine_sum >= k:
      return answer
  return 1


k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))

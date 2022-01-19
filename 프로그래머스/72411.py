# 프로그래머스 No.72411 메뉴 리뉴얼
"""
1. 글자 수에 따른 조합을 저장해준다.
2. 조합에 빈도 수를 세어준다.
3. 빈도 수가 가장 높은 조합들을 answer에 저장한다.
"""
from itertools import combinations
from collections import Counter

def solution(orders, course):
  answer = []

  for c in course:
    candidates = []
    for order in orders:
      combi = combinations(sorted(order),c)
      candidates += combi
    counter = Counter(candidates)

    if counter and max(counter.values()) > 1:
      answer += [''.join(item) for item, value in counter.items() if value == max(counter.values())]

  return sorted(answer)

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,4]
print(solution(orders, course))
# 백준 No.1759 암호 만들기
import sys
from itertools import combinations
"""
조합, 브루트 포스
1. alpha의 모든 경우의 수를 combi_list에 저장한다.
2. combi_list의 combi를 순환하며 모음과 자음의 개수를 세어준다.
3. 모음이 1개 이상 자음이 2개 이상 존재하며 answer에 combi를 저장한다.
4. answer를 순환하며 정답을 출력한다.
"""
def solution(l, c, alpha):
  answer = []
  combi_list = list(combinations(alpha, l))

  for combi in combi_list:
    vowel, consonant = 0, 0
    for s in combi:
      if s in ['a', 'e', 'i', 'o', 'u']:
        vowel += 1
      else:
        consonant += 1
      if vowel > 0 and consonant > 1:
        answer.append(''.join(combi))
        break
  return answer

l, c = map(int, sys.stdin.readline().split())
alpha = sorted(list(sys.stdin.readline().split()))
# l, c = 4, 6
# alpha = ['a', 't', 'c', 'i', 's', 'w']

for item in solution(l, c, alpha):
  print(item)
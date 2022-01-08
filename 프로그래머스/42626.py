# 프로그래머스 No.42626 더 맵게

"""
1. scoville 배열을 힙 자료구조로 변경한다.
2. 가장 작은 값이 K보다 큰지 확인한다.
3. scoville 배열의 길이가 2보다 작은지 확인한다.
4. 첫번째로 작은 scoville과 두번째로 작은 scoville을 힙의 성질을 이용하여 꺼낸다.
5. 문제에서 제시한 식에 맞게 first, second를 계산한 후에 scoville에 넣어준다.
6. 2의 과정을 반복한다.
"""

import heapq

def calcShakeScoville(first, second):
    return first + (second * 2)

def solution(scoville, K):
  answer = 0
  heapq.heapify(scoville)

  while scoville[0] < K:
    if len(scoville) < 2:
      return -1
    else:
      first = heapq.heappop(scoville)
      second = heapq.heappop(scoville)
      heapq.heappush(scoville, calcShakeScoville(first, second))
      answer += 1
  return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))

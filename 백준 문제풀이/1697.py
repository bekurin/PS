# 백준 1697번 숨바꼭질(BFS)
from collections import deque

n, k = map(int, input().split())

MAX = 100001
array = [0] * MAX

def bfs():
  q = deque([n])
  while q:
    nowPos = q.popleft()
    if nowPos == k:
      return array[nowPos]
    
    # 현재값 -1, 현재값 +1, 현재값 * 2을 선택한다.
    for nextPos in (nowPos-1, nowPos+1, nowPos*2):
      if 0 <= nextPos < MAX and not array[nextPos]:
        array[nextPos] = array[nowPos] + 1
        q.append(nextPos)
print(bfs())
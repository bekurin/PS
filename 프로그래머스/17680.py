# 프로그래머스 17680 [1차] 캐시
"""
데크, 구현
1. cities의 아이템을 모두 소문자로 바꿔준다.
2. cities를 순환하며 cache에 값이 있는지 확인한다.
3. 2의 결과가 참이라면 hit이기 때문에 현재 city의 값을 cache에서 지워준다.
4. 2의 결과가 거짓이라면 miss이기 때문에 cache에서 우선순위가 가장 높은 아이템을 제거해준다.
5. 현재 city의 값을 cache에 넣어준다.

데크의 maxlen을 사용하면 아래의 코드를 제외할 수 있다.
...
cache = deque(maxlen=cache_size)
...
if len(cache) >= cache_size:
  cache.popleft()
...
"""
from collections import deque

def solution(cache_size, cities):
  answer = 0
  cache = deque()
  cities = [city.lower() for city in cities]

  if cache_size == 0: return len(cities) * 5

  for city in cities: # cache hit
    if city in cache:
        answer += 1
        cache.remove(city)
    else: # cache miss
        answer += 5
        if len(cache) >= cache_size:
          cache.popleft()
    cache.append(city)
    print(cache)
  return answer

cache_size = 3
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cache_size, cities))
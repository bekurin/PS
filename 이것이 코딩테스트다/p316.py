import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
      return -1
    
    q = []
    for i in range(len(food_times)):
      heapq.heappush(q, (food_times[i], i+1))
    sumValue = 0
    previous = 0
    length = len(food_times)

    while sumValue + ((q[0][0]-previous) * length) <= k:
      now = heapq.heappop(q)[0]
      sumValue += (now - previous) * length
      length -= 1
      previous = now

    result = sorted(q ,key = lambda x: x[1])
    return result[(k-sumValue) % length][1]


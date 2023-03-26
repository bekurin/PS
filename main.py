# 프로그래머스 No.150369 택배 배달과 수거하기

# 차가 실을 수 있는 최고 택배 개수 cap
# 몇번을 왔다갔다 해야하나? 수거 택배, 배달 택배 중 총합이 많은 택배에서 (택백 / cap) 나누어 떨어지지 않는다면 +1
# 또는 반복문을 돌며 수거와 배달 택배의 총합을 계산하여 수거, 배달의 총합이 가장 많게 유지하면 배달을 시작한다. (그리디)
from collections import deque

def solution(cap, n, deliveries, pickups):
  answer = -1
  packages = list(zip(deliveries, pickups))

  queue = deque()
  delivery, pickup = 0, 0
  for idx, (package) in enumerate(packages):
    distance = idx + 1
    n_delivery, n_pickup = package
    n_delivery = delivery + n_delivery
    n_pickup = pickup + n_pickup

    delivery = n_delivery
    pickup = n_pickup
    if n_delivery >= cap or n_pickup >= cap:
      queue.append((distance, n_delivery, n_pickup))
      delivery, pickup = 0, 0
     
  print(list(queue))
  return answer

print(solution(
  4, 5, 
  [1, 0, 3, 1, 2],
  [0, 3, 0, 4, 0]
))
# 프로그래머스 No.150369 택배 배달과 수거하기
def solution(cap, n, deliveries, pickups):
  answer, delivery, pickup = 0, 0, 0
  deliveries = deliveries[::-1]
  pickups = pickups[::-1]

  for i in range(n):
    delivery += deliveries[i]
    pickup += pickups[i]

    while delivery > 0 or pickup > 0:
      delivery -= cap
      pickup -= cap
      answer += (n - i) * 2
  return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))

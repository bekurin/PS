# 프로그래머스 No.62048  멀쩡한 사각형
"""
최대공약수, 패턴 찾기
계산식: (w + h) - (w + h - gcd)

w, h를 최대공약수로 나눈 w', h'이 존재
이때, 모서리에서 모서리로 끝나는 하나의 패턴에는 w'-1의 세로선, h'-1의 가로선을 지난다.
선을 지날 때마다 새로운 잘린 사각형이 추가된다.
따라서 패턴 한번에 잘린 사각형의 수는 (w'-1)+(h'-1)+1 마지막 +1은 첫 사각형은 포함하여 계산한 것
결과적으로 최대공약수 만큼 패턴이 반복되기 때문에 잘린 사각형의 전체 수는 ((w'-1) + (h'-1) + 1) * gcd
gcd를 분배하여 식을 정리하면 (w + h - gcd)가 된다.
"""

# 팁을 얻은 후
def getGcd(w, h):
  while h != 0:
    r = w % h
    w = h
    h = r
  return w

def solution(w, h):
  if w == h:
    return (w * h) - w
  else:
    gcd = getGcd(w, h)
    return (w * h) - (w + h - gcd)

w = 3
h = 6
print(solution(w, h))

# 틀린 답
def solution(w, h):
    if w == h:
        return (w * h) - w
    else:
        left = h % 3
        share = h // 3

        if left == 1:
            return (w * h) - (share * 4 + 1)
        elif left == 2:
            return (w * h) - (share * 4 + 3)
        else:
            return (w * h) - (share * 4)
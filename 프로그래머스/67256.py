# 프로그래머스 No.67256 키패드 누르기
def solution(numbers, hand):
  answer = ''
  left, right = 10, 12

  for number in numbers:
    if number == 0: number = 11
    if number % 3 == 1:
      answer += "L"
      left = number
    elif number % 3 == 0:
      answer += "R"
      right = number
    else:
      dl = sum(divmod(abs(number - left), 3))
      dr = sum(divmod(abs(number - right), 3))
      # 오른손이 더 가까울 때
      if dl > dr:
        answer += "R"
        right = number
      elif dl < dr:
        answer += "L"
        left = number
      else:
        if hand == "right":
          answer += "R"
          right = number
        else:
          answer += "L"
          left = number
  return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))
print("LRLLRRLLLRR")
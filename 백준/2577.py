# 백준 No.2577 숫자의 개수
def solution(number_list):
  answer_list = [0] * 10
  for number in number_list:
    answer_list[int(number)] += 1
  return answer_list

a = int(input())
b = int(input())
c = int(input())

for item in solution(str(a * b * c)):
  print(item)
# 백준 No.18870 좌표 압축

def solution(n, number_list):
  answer_dict = {}
  sorted_list = sorted(set(number_list))

  answer_dict = {sorted_list[i]: i for i in range(len(sorted_list))}
  for number in number_list:
    print(answer_dict[number], end=" ")

n = int(input())
number_list = list(map(int, input().split()))
solution(n, number_list)
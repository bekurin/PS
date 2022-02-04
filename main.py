# 백준 No.6603 로또
import sys
input = sys.stdin.readline

def dfs(index, numbers, number_list):

  if len(numbers) == 6:
    for number in numbers:
      print(number, end = " ")
    print("")
    return

  if (6 - len(numbers)) - 1 <= (len(number_list) - (index + 1)):
    # 골라야 할 숫자의 개수 <= 남아 있는 숫자의 개수
    for i in range(index, len(number_list)):
      numbers.append(number_list[i])
      dfs(i + 1, numbers, number_list)
      numbers.pop()
  
number_list = []
while True:
  number_list = list(map(int, input().split()))

  if number_list[0] == 0: break
  number_list = number_list[1:]

  dfs(0, [], number_list)
  print("")

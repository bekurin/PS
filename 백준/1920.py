# 백준 No.1920 수 찾기

import sys
input = sys.stdin.readline

def binary_search(target, left, right):

  if left > right:
    return 0
  
  mid = (left + right) // 2
  if number_list[mid] == target:
    return 1
  elif number_list[mid] > target: 
    # target is left
    return binary_search(target, left, mid - 1)
  else:
    return binary_search(target, mid + 1, right)  

number_list, search_list = [], []

n = int(input())
number_list = sorted(list(map(int, input().split())))

m = int(input())
search_list = list(map(int, input().split()))

for search in search_list:
  print(binary_search(search, 0, len(number_list)-1))
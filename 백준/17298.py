# 백준 No.17298 오큰수
"""
스택, 자료구조
number_list를 순환하며 현재 stack의 마지막 값보다 큰 number가 있을 경우 stack에 값들을 확인하며 stack에서 number보다 큰 값이 나올 때까지 answer_list의 값을 초기화해준다.
"""
import sys
input = sys.stdin.readline

n = int(input())
answer_list = [-1] * n
number_list = list(map(int, input().split()))

stack = []
for i, number in enumerate(number_list):
  while stack and number_list[stack[-1]] < number:
    index = stack.pop()
    answer_list[index] = number
  stack.append(i)

for answer in answer_list:
  print(answer, end = " ")
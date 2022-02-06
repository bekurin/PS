# 백준 No.17219 비밀번호 찾기
"""
해시, 딕셔너리
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

id_pw_dict = {}
for _ in range(n):
  id, pw = input().split()
  id_pw_dict[id] = pw

search_list = []
for _ in range(m):
  search_list.append(input().strip())

for search in search_list:
  print(id_pw_dict[search])
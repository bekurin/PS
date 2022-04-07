# 백준 No.10773 제로
n = int(input())
answer_list = []
for _ in range(n):
  data = int(input())
  answer_list.append(data) if data != 0 else answer_list.pop()
print(sum(answer_list))
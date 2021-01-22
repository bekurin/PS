# 백준 1912번 연속합 (다이나믹 프로그래밍)
n = int(input())
data = list(map(int, input().split()))

answer = [data[0]]

for j in range(1, n):
  answer.append(max(answer[j-1] + data[j], data[j]))
print(max(answer))
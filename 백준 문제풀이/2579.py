# 백준 2579번 계단 오르기 (다이나믹 프로그래밍)
n = int(input())
data = [0] * 301
answer = [0] * 301
for i in range(1,n+1):
  data[i] = (int(input()))
answer[0] = 0
answer[1] = data[1]
answer[2] = max(data[0] + data[2], data[1] + data[2])
for i in range(3,n+1):
  answer[i] = max(answer[i-2] + data[i], answer[i-3] + data[i-1] + data[i])
print(answer[n])
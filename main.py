# 백준 No.1931 회의실 배정
"""
시작 시간과 끝나는 시간이 같은 회의가 존재하기 때문에 다음과 같이 정렬을 실행한다.
1. 시작 시간을 기준으로 정렬을 실행한다.
2. 종료 시간을 기준으로 정렬을 실행한다.
schedule을 순환하며 시작시간이 마지막 종료 시간보다 크거나 같다면 정답을 늘려주고, 마지막 종료 시간을 초기화해준다.
"""
def solution(schedule):
  answer = 0
  schedule = sorted(schedule, key=lambda x: x[0])
  print(schedule)
  schedule = sorted(schedule, key=lambda x: x[1])
  print(schedule)

  last_end = 0
  for start, end in schedule:
    if start >= last_end:
      answer += 1
      last_end = end 
  return answer

# n = int(input())
# schedule = []
# for _ in range(n):
#   schedule.append(list(map(int, input().split())))
# print(len(solution(schedule)))

schedule = [
  [1,4],
  [3,5],
  [5,7],
  [6,10],
  [6,6],
  [8,11],
  [2,13],
  [12,14]
]
print(solution(schedule))
# 백준 No.11723 집합
"""
1. item을 입력 받는다.
2. itme의 길이가 1이라면 all, check 명령어를 처리해준다.
3. item의 길이가 2 이상이라면 나머지 명령어를 처리해준다.
"""
import sys
input = sys.stdin.readline

# 함수로 추출한 코드
def solution(command, value, answer):
  if command == "add":
    answer.add(value)
  elif command == "check":
    print(1 if value in answer else 0)
  elif command == "remove":
    answer.discard(value)
  elif command == "toggle":
    if value in answer:
      answer.discard(value)
    else:
      answer.add(value)
  return answer

# 입력 부분
n = int(input())
command_list = []
for _ in range(n):
  command_list.append(input().split())

# 테스트 케이스
n = 10
command_list = [['add', '1'], ['add', '2'], ['check', '1'], ['check', '2'], ['check', '3'], ['remove', '2'], ['check', '1'], ['check', '2'], ['toggle', '3'], ['check', '1'], ['all'], ['empty']]
print(solution(command_list))

# 백준 성공 코드
n = int(input())
answer = set()
for _ in range(n):
  item = input().split()

  if len(item) == 1:
    answer = set([i for i in range(1, 21)]) if item[0] == "all" else set()
  else:
    command, value = item[0], int(item[1])
    answer = solution(command, value, answer)
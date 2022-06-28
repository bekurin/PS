# 프로그래머스 No.42883 큰 수 만들기
def solution(number, k):
  stack = []
  for num in number:
    while stack and stack[-1] < num and k > 0:
      k -= 1
      stack.pop()
    stack.append(num)
  if k != 0:
    stack = stack[:-k]
  return "".join(stack)

number = "1231234"
k = 3
print(solution(number, k))
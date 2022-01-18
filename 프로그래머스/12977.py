# 프로그래머스 No.12977 소수 만들기
def is_prime(num):
  if num <= 2:
    return False if num == 1 else True

  for i in range(2, num // 2 + 1):
    if num % i == 0:
      return False
  return True

def solution(nums):
  answer = 0
  numbers = []
  for i, num in enumerate(nums):
    for j in range(i+1, len(nums)):
      for k in range(j+1, len(nums)):
        numbers.append(nums[i] + nums[j] + nums[k])

  for number in numbers:
    if is_prime(number):
      answer += 1
  return answer

nums = [1,2,7,6,4]
print(solution(nums))
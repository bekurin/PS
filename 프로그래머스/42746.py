# 프로그래머스 No.42746 가장 큰 수

# 내가 작성한 풀이 (실패)
def solution(numbers):
  numbers = sorted(numbers, key = lambda x: (getUnit(x)), reverse=True)

  return str(int("".join(map(str, numbers))))

def getUnit(number):
  temp = len(str(number)) - 1
  print(number / 10**(temp)) 
  return number // 10**temp, number / 10**(temp), -temp

testCase = [3, 30, 34, 5, 9]	
print(solution(testCase))


# 참고한 풀이 (성공)
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
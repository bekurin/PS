# 프로그래머스 No.17682 다트 게임
"""
구현, 배열
1. dartResult의 'S', 'D', 'T' 값을 모두 정수로 바꿔준다.
2. 1의 결과를 순환한다.
3. 2의 결과가 '#'일 때 -1을 곱해준다.
4. 2의 결과가 '*'일 때 index의 값에 따라 값을 *2 해준다.
5. 2를 반복한다.
6. 5의 결과를 sum()을 사용하여 결과로 반환한다. 
"""
def solution(dartResult):
  formula = []
  temp = ''
  sdt = ['S', 'D', 'T']

  for s in dartResult:
    if s.isdigit():
      temp += s
    elif s in sdt:
      formula.append(int(temp) ** (sdt.index(s) + 1))
      temp = ''
    else:
      formula.append(s)

  for i, item in enumerate(formula):
    if item == '#':
      formula.pop(i)
      formula[i-1] = -formula[i-1]
    elif item == '*':
      formula.pop(i)
      if i < 2:
        formula[i-1] = formula[i-1] * 2
      else:
        formula[i-1] = formula[i-1] * 2
        formula[i-2] = formula[i-2] * 2
  return sum(formula)

dartResult = "1D#2S*3S"
print(solution(dartResult))
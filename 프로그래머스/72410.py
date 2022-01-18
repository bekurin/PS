# 프로그래머스 No.72410 신규 아이디 추천
"""
문제에서 제시한 단계에 따라서 문자열 처리를 해주는 문제
step.06의 경우 첫번째 문자가 '.'일 확률은 없으므로 처리 후 마지막 문자에 대해서만 처리해준다.
"""
def solution(new_id):
  answer = ''
  # step.01
  new_id = new_id.lower()

  # step.02
  for s in new_id:
    if s.isalnum() or s in ['-', '_', '.']:
      answer += s
  
  # step.03
  while '..' in answer:
    answer = answer.replace('..', '.')
  
  # step.04
  if answer[0] == '.':
    answer = answer[1:] if len(answer) > 1 else '.'
  if answer[-1] == '.':
    answer = answer[:-1]

  # step.05
  if not answer:
    answer = 'a'
  
  # step.06
  if len(answer) > 15:
    answer = answer[:15]
    if answer[-1] == '.':
      answer = answer[:-1]
  
  # step.07
  while len(answer) < 3:
    answer += answer[-1]
  return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))
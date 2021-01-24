def solution(participant, completion):
  participant.sort()
  completion.sort()
  answer = ""
  for i in range(len(participant)):
    if participant[i] != completion[i]:
      return participant[i]
  return answer

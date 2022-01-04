# 프로그래머스 No.42576 완주하지 못한 선수

"""
1. participant, completion 이름순으로 정렬한다.
2. participant와 completion을 순서대로 확인하며 이름이 다른 부분이 있는지 확인한다.
3. 이름이 다른 부분이 있다면 해당 선수가 완주하지 못한 선수이므로 결과로 반환한다.
4. 반복문이 끝난 후에도 결과를 반환하지 않았다면 participant 마지막 선수가 완주하지 못한 선수이므로 결과로 반환한다.
"""

def solution(participant, completion):
  participant.sort()
  completion.sort()

  for i in range(len(completion)):
    if (participant[i] != completion[i]):
      return participant[i]
  return participant[len(participant)-1]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))
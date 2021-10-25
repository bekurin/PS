# 프로그래머스 no.42747 H-index

def solution(citations):
  citations.sort()
  answer = 0

  for i in range(len(citations)):
    for j in range(i+1, len(citations)):
      if citations[i] <= citations[j]:
        count = len(citations) - j + 1
        break
    if count == citations[i]:
      answer = count

  return answer


testCase = [3, 0, 6, 1, 5]	
print(solution(testCase))
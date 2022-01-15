# 프로그래머스 No.92334 신고 결과 받기
"""
1. report에 중복을 제거하고, 신고자와 신고 당한 사람으로 나눈다.
2. report를 순환하며 나를 신고한 이용자의 id를 report_dict에 저장한다.
3. report_dict의 key를 순환하며 value의 길이가 k보다 큰 건에 한해서 해당 report_dict[key](나를 신고한 이용자) 값을 순환하며 repoted_dict(내가 받아야할 메일 개수)의 값을 1씩 올려준다.
"""

def solution(id_list, report, k):
  report = [item.split() for item in list(set(report))]
  answer_dict = {id:0 for id in id_list}
  report_dict = {id:[] for id in id_list}

  for reporter, target in report:
    report_dict[target].append(reporter)

  for key in report_dict.keys():
    if len(report_dict[key]) >= k:
      for value in report_dict[key]:
        answer_dict[value] += 1
  
  return list(answer_dict.values())

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))
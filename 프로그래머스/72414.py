# 프로그래머스 No.72414 순위 검색
from itertools import combinations

def get_processed_info(info):
  info = info.split(' ')
  return int(info[-1]), info[:-1]

def get_processed_query(query):
  query = [item for item in query.split(' ') if item != 'and']
  return int(query[-1]), ''.join(query[:-1])

def get_lower_bound(data, score):
  left = 0
  right = len(data)

  while left < right:
    mid = (left + right) // 2
    if (data[mid] < score):
      left = mid + 1
    else:
      right = mid
  return right

def solution(info, query):
  answer = []
  data = {}
  
  for item in info:
    score, conditions = get_processed_info(item)

    for i in range(5):
      for combination in combinations(range(4), i):
        temp_conditions = conditions.copy()
        for c in combination:
          temp_conditions[c] = '-'
        case = ''.join(temp_conditions)

        if case in data:
          data[case].append(score)
        else:
          data[case] = [score]
        
  for value in data.values():
    value.sort()
  
  for item in query:
    score, query = get_processed_query(item)
    
    if query in data:
      lower_bound = get_lower_bound(data[query], score)
      answer.append(len(data[query]) - lower_bound)
    else:
      answer.append(0)
  return answer    

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))



# def get_processed_info(info):
#     return info.split(' ')

# def get_processed_query(query):
#     query = query.split(' ')
#     return list(filter(is_and, query))

# def is_and(item):
#     if item == 'and':
#         return False
#     return True

# def is_valid_info(info, query):
#     for i in range(4):
#         if query[i] == '-':
#             continue
#         elif info[i] != query[i]:
#             return False
#     return int(info[-1]) >= int(query[-1])

# def solution(info, query):
#     answer = []
#     count = 0

#     info_list = [get_processed_info(item) for item in info]
#     query_list = [get_processed_query(item) for item in query]

#     for query in query_list:
#         count = 0
#         for info in info_list:
#             count += 1 if is_valid_info(info, query) else 0
#         answer.append(count)
#     return answer
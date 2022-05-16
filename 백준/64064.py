# 프로그래머스 No.64064 불량 사용자
def match_pattern(user, banned):
  if len(user) != len(banned):
    return False

  for i in range(len(user)):
    if banned[i] == '*': continue
    elif user[i] != banned[i]: return False
  return True

def get_candidate_list(user_id, banned_id):
  candidate_list = []
  for banned in banned_id:
    candidates = []
    for user in user_id:
      if match_pattern(user, banned):
        candidates.append(user)
    candidate_list.append(candidates)
  return candidate_list

def bfs(candidate_list, target, current, index):
  global case_list
  if len(current) == target:
    case_list.append(current[:])
    return

  for i in range(index, len(candidate_list)):
    for candidate in candidate_list[i]:
      if candidate not in current:
        current.append(candidate)
        bfs(candidate_list, target, current, i + 1)
        current.pop()

def is_avaiable(answer, case):
  for item_list in answer:
    count = 0
    for item in item_list:
      if item in case: count += 1
    if count == len(case): return False
  return True
        
case_list = []
def solution(user_id, banned_id):
  global case_list
  case_list = []
  
  candidate_list = get_candidate_list(user_id, banned_id)
  bfs(candidate_list, len(banned_id), [], 0)

  answer = []
  for case in case_list:
    if not answer:
      answer.append(case)
    elif is_avaiable(answer, case):
      answer.append(case)    
  return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id_list = [
  ["fr*d*", "abc1**"],
  ["*rodo", "*rodo", "******"],
  ["fr*d*", "*rodo", "******", "******"]
]
for banned_id in banned_id_list:
  print(solution(user_id, banned_id))

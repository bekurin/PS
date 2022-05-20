# 프로그래머스 No.67258 [카카오 인턴] 보석 쇼핑
def get_dict_and_count(gems):
  gem_dict = {}
  for item in set(gems):
    gem_dict[item] = 0
  return gem_dict, len(gem_dict.keys())

def is_minimum(right, left, current):
  if right - left < current[1] - current[0]:
    return True
  return False

def solution(gems):
  answer = [0, len(gems)]
  gem_dict, count = get_dict_and_count(gems)
  left, right = 0, 0

  while left <= right and right < len(gems):
    if 0 not in gem_dict.values():
      gem_dict[gems[left]] -= 1
      left += 1
      if is_minimum(right, left, answer):
        answer = [left, right]
    elif right < len(gems):
      gem_dict[gems[right]] += 1
      right += 1
    else:
      return answer
  return answer

gems = 	["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))
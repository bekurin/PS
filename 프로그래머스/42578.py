# 프로그래머스 No.42578 위장
def get_cloth_dict(clothes):
  cloth_dict = {}
  for cloth, category in clothes:
    if category not in cloth_dict:
      cloth_dict[category] = [cloth]
    else:
      cloth_dict[category].append(cloth)
  return cloth_dict

def solution(clothes):
  answer = 1
  cloth_count = []

  for key, value in get_cloth_dict(clothes).items():
    cloth_count.append(len(value))

  for count in cloth_count:
    answer *= (count + 1)
  return answer - 1

clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"], ["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
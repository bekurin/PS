# 프로그래머스 No.81301 숫자 문자열과 영단어

"""
dictionary
1. 주어진 문자를 순환하며 숫자인지 판별한다.
2. 숫자라면 answer에 현재 문자를 더해준다.
3. 숫자가 아니라면 temp에 현재 문자를 더해준다.
4. 숫자 문자열과 영단어 dictionary에 temp 값이 있는지 확인한다.
5. 4가 참이라면 dictionary의 value 값을 answer에 더해준다.
6. 4가 거짓이라면 1을 반복한다.
"""
number_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

# 0.2ms ~ 0.4ms
def solution(s):
  answer = ""

  temp = ""
  for char in s:
    if char.isdigit():
      answer += char
      temp = ""
    else:
      temp += char

    if temp in number_dict:
      answer += number_dict[temp]
      temp = ""
  return int(answer)

# 0.2ms
def solution_best(s):
    answer = s
    for key, value in number_dict.items():
        answer = answer.replace(key, value)
    return int(answer)

s = "one4seveneight"
print(solution(s))
# 프로그래머스 No.17684 [3차] 압축
def solution(msg):
  answer = [0]
  alphabet_dict = {}
  for number in range(0, 26):
    alphabet = chr(number + 65)
    alphabet_dict[alphabet] = number + 1
  
  word, value = "", 26
  for i in range(len(msg)):
    word += msg[i]
    if not word in alphabet_dict:
      value += 1
      alphabet_dict[word] = value
      word = msg[i]
      answer.append(alphabet_dict[word])
    else:
      answer[-1] = alphabet_dict[word]
  return answer


msg = "KAKAO"
print(solution(msg))

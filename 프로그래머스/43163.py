# 프로그래머스 No.43163 단어 변환
def is_possible(begin, target):
  count = 0
  index = max(len(begin), len(target))

  for i in range(index):
    if begin[i] != target[i]:
      count += 1
    if count > 1: return False
  return True if count == 1 else False

def dfs(word_list, words, begin, target):
  global answer
  if (len(word_list)) == len(words):
    return

  for word in words:
    if (is_possible(begin, word)) and word not in word_list:
      if word == target: answer = min(answer, len(word_list) + 1)
      word_list.append(word)
      dfs(word_list, words, word, target)
      word_list.pop()

answer = 51
def solution(begin, target, words):
  global answer
  if target not in words: return 0
  dfs([], words, begin, target)
  return answer
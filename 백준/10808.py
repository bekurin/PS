# 백준 No.10808 알파벳 개수
import sys
input = sys.stdin.readline

def solution(word):
  word_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
  
  for ch in word:
    word_dict[ch] += 1
  return word_dict

word = input().strip()
for key, value in solution(word.lower()).items():
  print(value, end=" ")
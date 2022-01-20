# 프로그래머스 17677 뉴스 클러스터링
"""
집합, 자카드 유사도
* 중복이 허용되는 집합
1. str1, str2를 순환하며 영문자에 한해 소문자로 변환하여 배열로 저장한다.
2. str1, str2의 합집합을 계산한다.
3. 합집합이 존재하지 않는다면 65536을 반환한다.
4. 합집합을 순환하며 str1, str2에서 개수를 비교한다.
5. 4의 과정에서 최대값은 합집합의 개수에 포함한다.
6. 4의 과정에서 최솟값은 교집합의 개수에 포함한다.
7. floor((6의 결과/5의 결과) * 65536)를 계산하여 결과를 반환한다.
"""
from math import floor

def solution(str1, str2):
  str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()]
  str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()]

  union = set(str1) | set(str2)

  if not union:
    return 65536

  union_sum = sum(max(str1.count(item), str2.count(item)) for item in union)
  inter_sum = sum(min(str1.count(item), str2.count(item)) for item in union)

  return floor(inter_sum/union_sum*65536)

str1 = "handshake"
str2 = "shake hands"
print(solution(str1, str2))
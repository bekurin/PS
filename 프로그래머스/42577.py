# 프로그래머스 No.42577 전화번호 목록
import heapq
def solution(phone_book):
  answer = True
  
  if len(phone_book) == 1:
    return answer

  heapq.heapify(phone_book)
  value = heapq.heappop(phone_book)
  while phone_book:
    length = len(value)
    if value == phone_book[0][:length]:
      return False
    value = heapq.heappop(phone_book)
  return answer

phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))
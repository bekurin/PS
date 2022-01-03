# 프로그래머스 No.42584 주식가격
def solution(prices):
  answer = [0] * len(prices)

  for i in range(len(prices)):
    for j in range(i+1, len(prices)):
      answer[i] += 1
      
      if prices[j] < prices[i]:
        break
  return answer

prices = [1,2,3,2,3]
print(solution(prices))
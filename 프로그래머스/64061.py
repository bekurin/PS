# 프로그래머스 64061번 크레인 인형뽑기 게임 (구현)
def solution(board, moves):
    basket = [0]
    n = len(board)
    count = 0

    for i in range(len(moves)):
      for j in range(n):
        # 만약 빈칸이 아니라면
        if board[j][moves[i]-1] != 0:
          prevValue = basket.pop()
          # 배열의 맨 위에 값과 현재값 비교
          if prevValue == board[j][moves[i]-1]:
            count += 2
          else:
            basket.append(prevValue)
            basket.append(board[j][moves[i]-1])
          board[j][moves[i]-1] = 0
          break
    return count
    
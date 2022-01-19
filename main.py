# 프로그래머스 No.17679 [1차] 프렌즈 4블록

def get_destoy_list(m,n,board):
  destroy = set()
  for x in range(m-1):
    for y in range(n-1):
      if board[x][y] == board[x+1][y] == board[x][y+1] == board[x+1][y+1] and board[x][y] != '0':
        destroy.add((x,y))
        destroy.add((x+1,y))
        destroy.add((x,y+1))
        destroy.add((x+1,y+1))
  return destroy if destroy else False

def get_falling_board(m,n,board):
  is_invalid = True

  while is_invalid:
    is_invalid = False
    for x in range(m-1):
      for y in range(n):
        if board[x+1][y] == '0' and board[x][y] != '0':
          is_invalid = True
          board[x][y], board[x+1][y] = '0', board[x][y]
  return board

def solution(m, n, board):
  answer = 0
  board = [list(item) for item in board]
  destroy_list = get_destoy_list(m,n,board)

  while destroy_list:
    answer += len(destroy_list)

    for x, y in destroy_list:
      board[x][y] = '0'
    board = get_falling_board(m, n, board)
    destroy_list = get_destoy_list(m,n,board)
  return answer

m = 6
n = 6
board = 	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	
print(solution(m,n,board))
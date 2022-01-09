# 프로그래머스 No.77485 행렬 테두리 회전하기
"""
category: 구현?
1. rows, columns를 이용하여 행렬을 만든다.
2. queries에서 item을 하나씩 가져와서 [x1, y1, x2, y2]로 치환한다.
3. 행렬의 회전에 의해 유실되는 행렬[x1-1][y1-1]의 값을 temp에 저장한다.
4. west -> south -> east -> north 순으로 행렬을 회전시킨다.
5. 4의 각 과정에서 최소값을 구해 mini에 초기화해준다. 
6. 행렬[x1-1][y1] 부분에 temp 값을 대입하고, answer에 mini를 추가해준다
7. 2의 과정을 반복한다.
"""

def getGrid(rows, columns):
  grid = []
  for row in range(rows):
    grid.append([column + (row * columns) for column in range(1, columns + 1)])
  return grid

def rotateWest(x1, y1, x2, y2, grid, mini):
  for i in range(x1 - 1, x2 - 1):
    grid[i][y1-1] = grid[i+1][y1-1]
    mini = min(mini, grid[i+1][y1-1])
  return mini

def rotateSouth(x1, y1, x2, y2, grid, mini):
  for i in range(y1 - 1, y2 - 1):
    grid[x2-1][i] = grid[x2-1][i+1]
    mini = min(mini, grid[x2-1][i+1])
  return mini

def rotateEast(x1, y1, x2, y2, grid, mini):
  for i in range(x2 - 1, x1 - 1, -1):
    grid[i][y2-1] = grid[i-1][y2-1]
    mini = min(mini, grid[i-1][y2-1])
  return mini

def rotateNorth(x1, y1, x2, y2, grid, mini):
  for i in range(y2 - 1, y1 - 1, -1):
    grid[x1-1][i] = grid[x1-1][i-1]
    mini = min(mini, grid[x1-1][i-1])
  return mini

def solution(rows, columns, queries):
  answer = []
  grid = getGrid(rows, columns)

  for x1, y1, x2, y2 in queries:
    temp = grid[x1-1][y1-1]
    mini = temp
    
    mini = rotateWest(x1, y1, x2, y2, grid, mini)
    mini = rotateSouth(x1, y1, x2, y2, grid, mini)
    mini = rotateEast(x1, y1, x2, y2, grid, mini)
    mini = rotateNorth(x1, y1, x2, y2, grid, mini)

    grid[x1-1][y1] = temp
    answer.append(mini)
  return answer


rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

print(solution(rows, columns, queries))
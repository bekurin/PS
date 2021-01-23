def rotateAMatrixBy90Degree(a):
  n = len(a)
  m = len(a[0])
  result = [[0] * n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result

def check(newLock):
  lockLength = len(newLock) // 3
  for i in range(lockLength, lockLength*2):
    for j in range(lockLength, lockLength*2):
      if newLock[i][j] != 1:
        return False
  return True

def solusion(key, lock):
  n = len(lock)
  m = len(key)

  newLock = [[0] * (n+3) for _ in range(n*3)]
  for i in range(n):
    for j in range(n):
      newLock[i+n][j+n] = lock[i][j]
    for rotation in range(4):
      key = rotateAMatrixBy90Degree(key)
      for x in range(n*2):
        for y in range(n*2):
          for i in range(m):
            for j in range(m):
              newLock[x+i][y+j] += key[i][j]
          if check(newLock) == True:
            return True
          for i in range(m):
            for j in range(m):
              newLock[x+i][y+j] -= key[i][j]
  return False
  
key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

print(solusion(key,lock))
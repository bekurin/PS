n = [44,1,0,0,31,25] # 나의 번호
m = [31,10,45,1,6,19] # 승리 번호

answer = []
rank = [6,6,5,4,3,2,1]
count = 0

for number in n:
  if number in m:
    count += 1

count0 = n.count(0)

answer.append(rank[count+count0])
answer.append(rank[count])

print(answer)
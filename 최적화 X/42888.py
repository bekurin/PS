# 프로그래머스 no.42888 오픈채팅방

def getFormat(command, userId):
  userIn = '{}님이 들어왔습니다.'
  userOut = '{}님이 나갔습니다.'

  if command == "Enter":
    return userIn.format(users[userId])
  elif command == "Leave":
    return userOut.format(users[userId])
  return None

def makeUserDict(data):
  if data[0] != "Leave":
    if data[0] == "Change" and users[data[1]]:
      users[data[1]] = data[2]
    else:
      users[data[1]] = data[2]

users = {}
def solution(record):
  answer = []
  commands = []
  for item in record:
    data = item.split(' ')
    makeUserDict(data)
    commands.append(data[:2])
  
  for command in commands: 
    answer.append(getFormat(command[0], command[1]))

  return list(filter(None, answer))

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
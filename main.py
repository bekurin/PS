# 프로그래머스 No.150366 표 병합

# 1. 표에서 병합 범위를 확인한다 (bfs 알고리즘을 사용)
# 2. 1의 결과를 사용하여 update, replace, merge를 처리한다.
# 3. unmerged 명령어라면 문제에 정의된 알고리즘을 사용하여 병합을 풀어준다.

def replace_table(table, target, replacement):
  for x in range(len(table)):
    for y in range(len(table)):
      if table[x][y] == target:
        table[x][y] = replacement
  return table


def update_table(table, r: int, c: int, value: str):
  r, c = int(r), int(c)
  table[r][c] = value
  return table


def merge_table(table, merge_info, r1, c1, r2, c2):
  r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
  for x in range(len(table)):
    for y in range(len(table)):
      if r1 <= x <= r2 and c1 <= y <= c2:
        merge_info[x][y] = 1
  return table, merge_info


def unmerge_table(table, r, c):
  print("unmerge!")
  return table


def print_table(table, r, c):
  r, c = int(r), int(c)
  return table[r][c]


def solution(commands):
  answer = []
  value_table = [[""] * 10 for _ in range(10)]
  merge_info = [[0] * 10 for _ in range(10)]
  for command in commands:
    elements = command.split(' ')
    if elements[0] == "UPDATE":
      if len(elements) == 3:
        target, replacement = elements[1], elements[2]
        value_table = replace_table(value_table, target, replacement)
      else:
        r, c, value = elements[1], elements[2], elements[3]
        value_table = update_table(value_table, r, c, value)
    elif elements[0] == "MERGE":
      r1, c1, r2, c2 = elements[1], elements[2], elements[3], elements[4]
      value_table, merge_info = merge_table(value_table, merge_info, r1, c1,
                                            r2, c2)
    elif elements[0] == "UNMERGE":
      r, c = elements[1], elements[2]
      unmerge_table(value_table, r, c)
    elif elements[0] == "PRINT":
      r, c = elements[1], elements[2]
      answer.append(print_table(value_table, r, c))
  print(value_table)
  print(merge_info)
  return answer


def bfs(merge_table, r, c):
  pass


commands = [
  "UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap",
  "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon",
  "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant",
  "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle",
  "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group",
  "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"
]
print(solution(commands))

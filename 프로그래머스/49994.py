# 프로그래머스 no.49994 방문 길이
def solution(dirs):
    x, y = 5, 5
    answer = set()
    for dir in dirs:
        nx, ny = move(x, y, dir)
        if not is_valid_move(nx, ny):
            continue
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        x, y = nx, ny
    return len(answer) / 2

def is_valid_move(nx, ny):
    return 0 <= nx < 11 and 0 <= ny < 11

def move(x, y, dir):
    if dir == 'U':
        nx, ny = x, y + 1
    elif dir == 'D':
        nx, ny = x, y - 1
    elif dir == 'L':
        nx, ny = x - 1, y
    elif dir == 'R':
        nx, ny = x + 1, y
    return nx, ny

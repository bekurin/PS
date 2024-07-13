# 프로그래머스 No.81303 표 편집
def solution(n, k, cmd):
    deleted = []
    
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]
    k += 1
    
    for cmd_item in cmd:
        if cmd_item.startswith('C'):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
            
        elif cmd_item.startswith('Z'):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
        else :
            action, count = cmd_item.split()
            if action == 'U':
                for _ in range(int(count)):
                    k = up[k]
            else:
                for _ in range(int(count)):
                    k = down[k]
    answer = ['O'] * n
    for deleted_index in deleted:
        answer[deleted_index - 1] = 'X'
    return "".join(answer)
                    
            
    
    return answer

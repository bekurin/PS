# 프로그래머스 No.12909 올바른 괄호

def solution(s):
    if len(s) % 2 != 0 or s[0] == ')':
        return False
    else:
        return is_right_pattern(list(s))


def is_right_pattern(bracket_list):
    stack = []
    for bracket in bracket_list:
        if bracket == '(':
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()
    return False if stack else True


s = "()()"
print(solution(s))
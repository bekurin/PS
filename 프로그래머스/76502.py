# 프로그래머스 No.76502 괄호 회전하기

def solution(s):
    answer = 0
    bracket = [('(', ')'), ('{', '}'), ('[', ']')]
    if is_available_bracket(s, bracket):
        return 0
    else:
        for candidate in get_candidate_list(s):
            for _, close in bracket:
                if candidate[0] == close:
                    continue
            if is_right_bracket_pattern(candidate, bracket):
                print("".join(candidate))
                answer += 1
    return answer


def is_available_bracket(s, bracket):
    for open, close in bracket:
        if not is_open_and_close_bracket_count_equal(s, open, close):
            return True
    return False


def is_open_and_close_bracket_count_equal(s, open, close):
    return s.count(open) == s.count(close)


def get_candidate_list(s):
    candidate, candidate_list = list(s), []
    for char in s:
        candidate.pop(0)
        candidate.append(char)
        candidate_list.append(candidate[:])
    return candidate_list


def is_right_bracket_pattern(candidate, bracket):
    stack = []
    for item in candidate:
        for open, close in bracket:
            if item == open:
                stack.append(open)
            if item == close:
                if not stack: return False
                pop = stack.pop()
                for open, close in bracket:
                    if pop == open and item != close: return False
    return False if stack else True


s = "[)(]"
print(solution(s))

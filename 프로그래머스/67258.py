# 프로그래머스 No.67258 보석 쇼핑

def solution(gems):
    answer, n = [1, len(gems)], len(set(gems))
    gem_dict = get_default_gem_dict(gems)

    left, right = 0, 1
    while left < right:
        if len(gem_dict) == n:
            gem_dict = remove_by(gem_dict, gems[left])
            left += 1
            answer = min_answer(answer, [left, right])
        elif right < len(gems):
            gem_dict = add_by(gem_dict, gems[right])
            right += 1
        else:
            break
    return answer


def add_by(gem_dict, item):
    if item in gem_dict:
        gem_dict[item] += 1
    else:
        gem_dict[item] = 1
    return gem_dict


def remove_by(gem_dict, item):
    if gem_dict[item] > 1:
        gem_dict[item] -= 1
    else:
        del gem_dict[item]
    return gem_dict


def min_answer(answer, candidate):
    if answer[1] - answer[0] > candidate[1] - candidate[0]:
        return candidate
    return answer


def get_default_gem_dict(gems):
    return {gems[0]: 1}


gems = ["A", "A", "B"]
print(solution(gems))

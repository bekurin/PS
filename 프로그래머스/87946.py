# 프로그래머스 No.87946 피로도
from itertools import permutations


def get_dungeon_count_by(max_fatigue, dungeon_list):
    count = 0
    fatigue = max_fatigue

    for require, consume in dungeon_list:
        if fatigue < require:
            continue
        fatigue -= consume
        count += 1
    return count


def get_case_list(dungeons):
    case_list = []
    length = len(dungeons)

    for item in list(permutations(range(length), length)):
        temp = []
        for idx in item:
            temp.append(dungeons[idx])
        case_list.append(temp)
    return case_list


def solution(k, dungeons):
    answer = 0
    for case in get_case_list(dungeons):
        answer = max(answer, get_dungeon_count_by(k, case))
    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))

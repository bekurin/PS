# 프로그래머스 No.118666 성격 유형 검사하기

score_list = [3, 2, 1, 0, 1, 2, 3]
couple_type = (('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N'))


def get_init_result_dict(couple_type):
    result_dict = {}
    for front, end in couple_type:
        result_dict[front], result_dict[end] = 0, 0
    return result_dict


def solution(survey, choices):
    result_dict = get_init_result_dict(couple_type)
    for i, item in enumerate(survey):
        result_dict[get_char(choices[i], item)] += score_list[choices[i] - 1]
    return get_answer_by(result_dict)


def get_char(choice, item):
    return item[0] if choice < 4 else item[1]


def get_answer_by(result_dict):
    answer = ''
    for front, end in couple_type:
        answer += front if result_dict[front] > result_dict[end] or result_dict[front] == result_dict[end] else end
    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))

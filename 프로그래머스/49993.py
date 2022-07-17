# 프로그래머스 No.49993 스킬트리

def solution(skill, skill_trees):
    answer = 0
    available_skill_trees = get_available_skill_tress(skill)
    candidate_list = get_processed_skill_trees(skill, skill_trees)

    for available in available_skill_trees:
        answer += candidate_list.count(available)
    return answer


def get_available_skill_tress(skill):
    available = [""]
    for idx in range(len(skill)):
        available.append(skill[:idx + 1])
    return available


def get_processed_skill_trees(skill, skill_trees):
    candidate = []
    for skill_tree in skill_trees:
        temp = ""
        for char in skill_tree:
            if char in skill:
                temp += char
        candidate.append(temp)
    return candidate


skill = "CBDK"
skill_trees = ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"]
print(solution(skill, skill_trees))
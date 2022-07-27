# 프로그래머스 No.84512 모음사전
candidate_list = []


def dfs(word_list, current):
    global candidate_list
    candidate_list.append(''.join(current[:]))

    if len(current) == len(word_list):
        return

    for idx in range(0, len(word_list)):
        current.append(word_list[idx])
        dfs(word_list, current)
        current.pop()


def solution(word):
    global candidate_list
    word_list = ['A', 'E', 'I', 'O', 'U']
    dfs(word_list, [])
    return candidate_list.index(word)


word = "I"
print(solution(word))

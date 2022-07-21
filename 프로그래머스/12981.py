# 프로그래머스 No.12981 영어 끝말잇기

def solution(n, words):
    answer = [0, 0]

    spoken_word_list = []
    pre_word = words[0][0]
    for idx, word in enumerate(words):
        participant = idx % n + 1
        n_th_word = idx // n + 1
        if pre_word[-1] != word[0] or word in spoken_word_list:
            return [participant, n_th_word]
        spoken_word_list.append(word)
        pre_word = word
    return answer


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))

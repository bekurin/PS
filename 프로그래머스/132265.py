# 프로그래머스 no.132265 롤케이크 자르기
from collections import Counter

def solution(topping):
    answer = 0
    
    topping_counter = Counter(topping)
    half_topping = set()
    
    for t in topping:
        half_topping.add(t)
        topping_counter[t] -= 1
        
        if topping_counter[t] == 0:
            topping_counter.pop(t)
        
        if len(half_topping) == len(topping_counter):
            answer += 1
    return answer

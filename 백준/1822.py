# 백준 No.1822 차집합
def solution(set_a, set_b):
    set_a = set(set_a)
    set_b = set(set_b)
    return set_a - set_b

a, b = map(int, input().split())
set_a = list(map(int, input().split()))
set_b = list(map(int, input().split()))

answer = solution(set_a, set_b)
count = len(answer)

print(count)
if count:
    for item in sorted(answer):
        print(item, end=" ")
# 백준 No.1644 소수의 연속합

def solution(n):
    prime_list = get_prime_list(n * 2)
    target = sum(prime_list)
    if target == n:
        return 1
    elif target < n:
        return 0
    elif target > n:
        return two_pointer(prime_list, n)


def two_pointer(prime_list, n):
    answer = 0
    total, right = 0, 0

    for left in range(len(prime_list)):
        while total < n and right < len(prime_list):
            total += prime_list[right]
            right += 1
        if total == n:
            answer += 1
        total -= prime_list[left]
    return answer


def get_prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

n = int(input())
print(solution(n))
# 백준 No.2512 예산
import sys
input = sys.stdin.readline


def binary_search(budget, target):
    left, right = 0, max(budget)
    while left <= right:
        mid = (left + right) // 2
        total = get_total_budget(budget, mid)

        if total > target:
            right = mid - 1
        elif total <= target:
            left = mid + 1
    return right


def get_total_budget(budget, mid):
    total = 0
    for i, item in enumerate(budget):
        if item >= mid:
            total += mid * (len(budget) - i)
            break
        else:
            total += item
    return total


def solution(budget, total):
    budget.sort()
    if sum(budget) <= total:
        return budget[-1]
    return binary_search(budget, total)

n = int(input())
budget = list(map(int, input().split()))
total = int(input())

print(solution(budget, total))
"""
    [문제 요약] 곱셈, 나눗셈, 나머지 연산 없이 두 정수의 몫 구하기
    [핵심 아이디어] 지수적 뺄셈 (Exponential Search / Bit Manipulation)
    1. 선형적으로 빼는 대신(O(N)), divisor를 2배씩 키우며 뭉텅이로 뺀다(O(log N^2)).
    2. 비트 시프트(<< 1)를 사용하여 '2배 곱하기' 연산을 대체한다.

    [주요 제약 조건 처리]
    - 부호 처리: XOR 연산 혹은 비교 연산으로 결과 부호를 미리 결정 후 절대값으로 계산.
    - 오버플로우: 32비트 정수 범위 [-2^31, 2^31 - 1] 준수.
      특히 (-2^31 / -1) 케이스는 결과값이 범위를 벗어나므로 예외 처리 필요.
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negative = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)

        quotient = 0

        while a >= b:
            temp_divisor = b
            count = 1
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1

            a -= temp_divisor
            quotient += count

        result = -quotient if negative else quotient
        return max(MIN_INT, min(MAX_INT, result))

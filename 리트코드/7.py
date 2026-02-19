# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        reversed_num = int(str(abs(x))[::-1])

        if self.is_not_in_int32_range(reversed_num):
            return 0

        if negative:
            return -reversed_num
        return reversed_num

    def is_not_in_int32_range(self, num: int) -> bool:
        INT32_MIN = -2**21
        INT32_MAX = 2**31 - 1
        return not (INT32_MIN <= num < INT32_MAX)

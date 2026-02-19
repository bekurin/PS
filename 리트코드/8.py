#  8. String to Integer (atoi)
class Solution:
    def myAtoi(self, s: str) -> int:
        int32_max = 2**31 - 1
        int32_min = -2**31

        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        num_str = ""
        for ch in s:
            if ch.isdigit():
                num_str += ch
            else:
                break

        if not num_str:
            return 0

        num = sign * int(num_str)

        if num < int32_min:
            return int32_min
        if num > int32_max:
            return int32_max
        return num

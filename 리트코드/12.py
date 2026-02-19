# 12. Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        thousands, rem = divmod(num, 1000)
        hundreds, rem = divmod(rem, 100)
        tens, ones = divmod(rem, 10)

        roman_thousands = ["", "M", "MM", "MMM"]
        roman_hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        roman_tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        roman_ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (
            roman_thousands[thousands]
            + roman_hundreds[hundreds]
            + roman_tens[tens]
            + roman_ones[ones]
        )

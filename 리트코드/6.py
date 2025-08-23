# 6. Zigzag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if self.is_pre_return_condition(s, numRows):
            return s

        rows = [""] * numRows
        row, direction = 0, 1

        for ch in s:
            rows[row] += ch
            row, direction = self.next_row(row, direction, numRows)

        return "".join(rows)

    def is_pre_return_condition(self, s: str, numRows: int):
        return numRows == 1 or numRows >= len(s)

    def next_row(self, row: int, direction: int, numRows: int) -> tuple[int, int]:
        if row == 0:
            direction = 1
        elif row == numRows - 1:
            direction = -1
        return row + direction, direction

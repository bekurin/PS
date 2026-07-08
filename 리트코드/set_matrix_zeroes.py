class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        # 1. 첫 번째 행과 열에 0이 있는지 확인
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True

        # 2. 나머지 행렬을 돌며 첫 번째 행/열을 전광판(플래그)으로 사용
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 3. 전광판 기록을 바탕으로 행렬의 값들을 0으로 변경
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 4. 최초에 첫 번째 행/열에 0이 있었다면 해당 행/열 전체를 0으로 변경
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

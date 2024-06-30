// 프로그래머스 no.68645 삼각 달팽이
class Solution {
    fun solution(n: Int): IntArray {
        val triangle = Array(n) { IntArray(n) }
        val dx = listOf(0, 1, -1)
        val dy = listOf(1, 0, -1)

        var (x, y) = Pair(0, 0)
        var (number, direction) = Pair(1, 0)

        while (true) {
            triangle[y][x] = number++
            var nx = x + dx[direction]
            var ny = y + dy[direction]

            if (nx == n || ny == n || triangle[ny][nx] != 0) {
                direction = (direction + 1) % 3
                nx = x + dx[direction]
                ny = y + dy[direction]

                if (nx == n || ny == n || triangle[ny][nx] != 0) {
                    break
                }
            }
            x = nx
            y = ny
        }

        return calculateAnswer(number, n, triangle)
    }

    private fun calculateAnswer(number: Int, n: Int, triangle: Array<IntArray>): IntArray {
        val answer = IntArray(number - 1)
        var index = 0
        for (i in 0 until n) {
            for (j in 0..i) {
                if (triangle[i][j] != 0) {
                    answer[index++] = triangle[i][j]
                }
            }
        }
        return answer
    }
}

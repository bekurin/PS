// 프로그래머스 No.68936 쿼드압축 후 개수 세기
class Solution {
    fun solution(arr: Array<IntArray>): IntArray {
        val answer = IntArray(2)
        compress(arr.size, 0, 0, answer, arr)
        return answer
    }

    private fun compress(size: Int, startX: Int, startY: Int, answer: IntArray, arr: Array<IntArray>) {
        if (size == 1) {
            answer[arr[startY][startX]]++
            return
        }

        if (isUniform(size, startX, startY, answer, arr)) {
            return
        }

        val halfSize = size / 2
        compress(halfSize, startX, startY, answer, arr)
        compress(halfSize, startX + halfSize, startY, answer, arr)
        compress(halfSize, startX, startY + halfSize, answer, arr)
        compress(halfSize, startX + halfSize, startY + halfSize, answer, arr)
    }

    private fun isUniform(size: Int, startX: Int, startY: Int, answer: IntArray, arr: Array<IntArray>): Boolean {
        val firstValue = arr[startY][startX]
        for (i in startY until startY + size) {
            for (j in startX until startX + size) {
                if (arr[i][j] != firstValue) {
                    return false
                }
            }
        }
        answer[firstValue]++
        return true
    }
}

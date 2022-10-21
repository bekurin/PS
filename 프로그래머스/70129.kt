package 프로그래머스

// 프로그래머스 No.70129 이진 변환 반복하기
class Solution {
    fun solution(s: String): IntArray {
        var count: Int = 0
        var removeZero: Int = 0
        var result: String = s

        while (result != "1") {
            count += 1
            removeZero += result.count { it == '0' }
            result = Integer.toBinaryString(result.count { it == '1'})
        }
        return intArrayOf(count, removeZero)
    }
}

fun main() {
    val s: String = "110010101001"
    println("Solution().solution(s) = ${Solution().solution(s)}")
}
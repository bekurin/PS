package 프로그래머스

// 프로그래머스 No.12944 평균 구하기
class Solution12944 {
    fun solution(arr: IntArray): Double {
        return (arr.sum().toDouble()) / arr.size
    }
}

fun main() {
    val arr = intArrayOf(1, 2, 3, 4)
    println(Solution12944().solution(arr))
}

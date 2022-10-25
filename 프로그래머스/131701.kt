package 프로그래머스

// 프로그래머스 No.131701 연속 부분 수열 합의 개수
class Solution131701 {
    private val cases = mutableSetOf<Int>()

    fun solution(elements: IntArray): Int {
        for ((idx, element) in elements.withIndex()) {
            dfs(elements, mutableListOf(element), (idx + 1) % elements.size)
        }
        return cases.size
    }

    private fun dfs(elements: IntArray, number: MutableList<Int>, visited: Int) {
        cases.add(number.sum())
        if (number.size == elements.size) {
            return
        }
        number.add(elements[visited])
        dfs(elements, number, (visited + 1) % elements.size)
    }
}

fun main() {
    val elements = intArrayOf(7, 9, 1, 1, 4)
    println(Solution131701().solution(elements))
}
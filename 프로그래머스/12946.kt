// 프로그래머스 No.12946 하노이의 탑
class Solution {
    fun solution(n: Int): Array<IntArray> {
        var answer = mutableListOf<IntArray>()
        val hanoi = hanoi(answer, n, 1, 3, 2)
        return answer.toTypedArray()
    }

    private fun hanoi(answer: MutableList<IntArray>, n: Int, from: Int, to: Int, aux: Int) {
        if (n == 1) {
            answer.add(intArrayOf(from, to))
            return
        }
        hanoi(answer, n - 1, from, aux, to)
        answer.add(intArrayOf(from, to))
        hanoi(answer, n - 1, aux, to, from)
    }
}

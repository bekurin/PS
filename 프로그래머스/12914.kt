package 프로그래머스

// 프로그래머스 No.12914 멀리 뛰기
fun getInitStepList(n: Int): LongArray {
    return LongArray(n) { 0 }
}


fun solution(n: Int): Long {
    val stepList = getInitStepList(n)

    for (idx in stepList.indices) {
        when (idx) {
            0 -> stepList[idx] = 1
            1 -> stepList[idx] = 2
            else -> stepList[idx] = (stepList[idx - 1] + stepList[idx - 2]).mod(1234567L)
        }
    }
    return stepList.last()
}


fun main() {
    println(solution(5))
}
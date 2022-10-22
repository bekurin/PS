package 프로그래머스

// 프로그래머스 No.12985 예상 대진표
fun solution(n: Int, a: Int, b: Int): Int {
    var answer = 0
    var targetA = a
    var targetB = b

    while (targetA != targetB) {
        targetA = (targetA + 1) / 2
        targetB = (targetB + 1) / 2
        answer += 1
    }
    return answer
}

fun main() {
    println(solution(8, 4, 7))
}
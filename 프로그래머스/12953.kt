package 프로그래머스

// 프로그래머스 No.12953 N개의 최소공배수
fun solution(arr: IntArray): Int {
    var answer = 0
    for (idx in 0 until (arr.size - 1)) {
        answer = lcm(arr[idx], arr[idx + 1])
        arr[idx + 1] = answer
    }
    return answer
}

fun lcm(n: Int, m: Int) = n * m / gcd(n, m)

fun gcd(n: Int, m: Int): Int {
    return if (n < m) {
        if (n == 0) m else gcd(n, m % n)
    } else {
        if (m == 0) n else gcd(m, n % m)
    }
}

fun main() {
    val result = solution(intArrayOf(2, 6, 8, 14))
    println("result = $result")
}
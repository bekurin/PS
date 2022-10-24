package 프로그래머스

// 프로그래머스 No.131127 할인 행사
fun solution(
    want: Array<String>,
    number: IntArray,
    discount: Array<String>
): Int {
    var answer: Int = 0
    val duration = number.sum()
    val lastDay = discount.size
    val basket = getBasketAsMap(want, number)

    for (startDay in discount.indices) {
        if (startDay + duration > lastDay) break
        val itemList = discount.slice(getIntRangeBy(startDay, duration, lastDay))
        answer += if (isValidCounter(getItemCounterAsMapBy(itemList), basket)) 1 else 0
    }
    return answer
}

private fun getBasketAsMap(
    want: Array<String>,
    number: IntArray
): MutableMap<String, Int> {
    val basket = mutableMapOf<String, Int>()
    for (idx in want.indices) {
        basket[want[idx]] = number[idx]
    }
    return basket
}

private fun getIntRangeBy(
    startDay: Int,
    duration: Int,
    lastDay: Int
): IntRange {
    return IntRange(startDay, (if (startDay + duration < lastDay) startDay + duration else lastDay) - 1)
}

private fun getItemCounterAsMapBy(
    itemList: List<String>
): MutableMap<String, Int> {
    val counter = mutableMapOf<String, Int>()
    for (element in itemList) {
        counter[element] = counter[element]?.plus(1) ?: 1
    }
    return counter
}

private fun isValidCounter(
    counter: MutableMap<String, Int>,
    wantMap: MutableMap<String, Int>
): Boolean {
    for (element in wantMap.keys) {
        if ((counter[element] ?: 0) < wantMap[element]!!) return false
    }
    return true
}

fun main() {
    val want = arrayOf("banana", "apple", "rice", "pork", "pot")
    val number = intArrayOf(3, 2, 2, 2, 1)
    val discount = arrayOf(
        "chicken",
        "apple",
        "apple",
        "banana",
        "rice",
        "apple",
        "pork",
        "banana",
        "pork",
        "rice",
        "pot",
        "banana",
        "apple",
        "banana"
    )
    println(solution(want, number, discount))
}
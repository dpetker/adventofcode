import java.io.File

val NUMBER_TO_DIGIT_MAP =
    mapOf(
        "one" to 1,
        "two" to 2,
        "three" to 3,
        "four" to 4,
        "five" to 5,
        "six" to 6,
        "seven" to 7,
        "eight" to 8,
        "nine" to 9,
        "1" to 1,
        "2" to 2,
        "3" to 3,
        "4" to 4,
        "5" to 5,
        "6" to 6,
        "7" to 7,
        "8" to 8,
        "9" to 9
    )

var part1RunningTotal = 0
var part2RunningTotal = 0

fun computePart1(line: String): Int {
  val firstDigit = line.filter { it.isDigit() }.firstOrNull()
  val lastDigit = line.reversed().filter { it.isDigit() }.firstOrNull()

  return "$firstDigit$lastDigit".toInt()
}

fun computePart2(line: String): Int {
  val firstMatch = line.findAnyOf(NUMBER_TO_DIGIT_MAP.keys)
  val lastMatch = line.findLastAnyOf(NUMBER_TO_DIGIT_MAP.keys)

  val firstDigit = NUMBER_TO_DIGIT_MAP[firstMatch!!.second]
  val lastDigit = NUMBER_TO_DIGIT_MAP[lastMatch!!.second]

  return "$firstDigit$lastDigit".toInt()
}

fun main() {
  val lineList = mutableListOf<String>()

  // The File() call is relative to the directory we're running run.sh from
  File("./input/day1.txt").useLines { lines -> lines.forEach { lineList.add(it) } }

  lineList.forEach { line ->
    part1RunningTotal += computePart1(line)
    part2RunningTotal += computePart2(line)
  }

  println("Part 1 total: $part1RunningTotal")
  println("Part 2 total: $part2RunningTotal")
}

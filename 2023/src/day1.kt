import java.io.File

fun main() {
  val lineList = mutableListOf<String>()

  // The File() call is relative to the directory we're running run.sh from
  File("./input/day1.txt").useLines { lines -> lines.forEach { lineList.add(it) } }

  var part1RunningTotal = 0

  lineList.forEach { line ->
    val firstDigit = line.filter { it.isDigit() }.firstOrNull()
    val lastDigit = line.reversed().filter { it.isDigit() }.firstOrNull()

    val twoDigit = "$firstDigit$lastDigit".toInt()

    part1RunningTotal += twoDigit
  }

  println("Part 1 total: $part1RunningTotal")
}

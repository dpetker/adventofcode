/*
Global variables for all available test data.

Globals aren't generally a good idea, but in this case it saves us from
re-reading this data multiple times.
*/

package internal

var Day1RealData []string = ReadPuzzleInput("./input/day1.txt")

var Day2SampleData []string = ReadPuzzleInput("./input/day2_sample.txt")
var Day2RealData []string = ReadPuzzleInput("./input/day2.txt")

var Day3SampleData []string = ReadPuzzleInput("./input/day3_sample.txt")
var Day3RealData []string = ReadPuzzleInput("./input/day3.txt")

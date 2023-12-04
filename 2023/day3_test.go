package main

import (
	"adventofcode/2023/internal"
	"fmt"
	"testing"
)

func TestDay3SampleDataPart1(t *testing.T) {
	expected := 4361

	day3 := CreateDay3(internal.Day3SampleData)
	result := day3.Part1()

	fmt.Println("Day 3 - Part 1 total (sample data):", result)

	if result != expected {
		t.Fatalf(`Day3.Part1() (sample data) = %d, wanted %d`, result, expected)
	}
}

func TestDay3SampleDataPart2(t *testing.T) {
	t.Skip()
	// expected := 2286

	// day2 := CreateDay2(sampleData)
	// result := day2.Part2()

	// fmt.Println("Day 2 - Part 2 total (sample data):", result)

	// if result != expected {
	// 	t.Fatalf(`Day2.Part1() (sample data) = %d, wanted %d`, result, expected)
	// }
}

func TestDay3RealDataPart1(t *testing.T) {
	t.Skip()
	// expected := 2600

	// day2 := CreateDay2(realData)
	// result := day2.Part1()

	// fmt.Println("Day 2 - Part 1 total:", result)

	// if result != expected {
	// 	t.Fatalf(`Day2.Part1() (sample data) = %d, wanted %d`, result, expected)
	// }
}

func TestDay3RealDataPart2(t *testing.T) {
	t.Skip()
	// expected := 86036

	// day2 := CreateDay2(realData)
	// result := day2.Part2()

	// fmt.Println("Day 2 - Part 2 total (sample data):", result)

	// if result != expected {
	// 	t.Fatalf(`Day2.Part1() (sample data) = %d, wanted %d`, result, expected)
	// }
}

package main

import (
	"adventofcode/2023/internal"
	"fmt"
	"testing"
)

func TestDay2SampleDataPart1(t *testing.T) {
	expected := 8

	day2 := CreateDay2(internal.Day2SampleData)
	result := day2.Part1()

	fmt.Println("Day 2 - Part 1 total (sample data):", result)

	if result != expected {
		t.Fatalf(`Day2.Part1() (sample data) = %d, wanted %d`, result, expected)
	}
}

func TestDay2SampleDataPart2(t *testing.T) {
	expected := 2286

	day2 := CreateDay2(internal.Day2SampleData)
	result := day2.Part2()

	fmt.Println("Day 2 - Part 2 total (sample data):", result)

	if result != expected {
		t.Fatalf(`Day2.Part2() (sample data) = %d, wanted %d`, result, expected)
	}
}

func TestDay2RealDataPart1(t *testing.T) {
	expected := 2600

	day2 := CreateDay2(internal.Day2RealData)
	result := day2.Part1()

	fmt.Println("Day 2 - Part 1 total:", result)

	if result != expected {
		t.Fatalf(`Day2.Part1() = %d, wanted %d`, result, expected)
	}
}

func TestDay2RealDataPart2(t *testing.T) {
	expected := 86036

	day2 := CreateDay2(internal.Day2RealData)
	result := day2.Part2()

	fmt.Println("Day 2 - Part 2 total:", result)

	if result != expected {
		t.Fatalf(`Day2.Part2() = %d, wanted %d`, result, expected)
	}
}

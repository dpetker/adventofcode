package main

import (
	"regexp"
)

type Day3 struct {
	engine Engine
}

type Engine struct {
	connectedParts   map[string][]int
	unconnectedParts []int
}

////////////////////////////////////////////////////////////////////////////////

/* Day-related methods */
func (d Day3) Part1() int {
	return 0
}

func (d Day3) Part2() int {
	return 0
}

func CreateDay3(lines []string) Day3 {
	engine := CreateEngine(lines)
	return Day3{engine}
}

////////////////////////////////////////////////////////////////////////////////

/* Engine-related methods */
func CreateEngine(lines []string) Engine {
	e := Engine{make(map[string][]int), []int{}}

	runeTest := regexp.MustCompile(`^(\.|\d)$`)
	for rowNum, line := range lines {
		for colNum, val := range line {
			valAsStr := string(val)
			if !runeTest.MatchString(valAsStr) {
				_, ok := e.connectedParts[valAsStr]
				if !ok {
					e.connectedParts[valAsStr] = []int{}
				}

				// TODO: search around valAsStr for numbers
			}
		}
	}

	return e
}

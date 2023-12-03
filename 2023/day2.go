// Day 2 - Now in Go!
package main

import (
	"fmt"
	"strconv"
	"strings"

	"adventofcode/2023/internal"
)

type Game struct {
	id     int
	rounds []Round
}

func (g Game) IsPossible(red int, green int, blue int) bool {
	for _, round := range g.rounds {
		if !round.IsPossible(red, green, blue) {
			return false
		}
	}
	return true
}

func (g Game) MinNeeded() []int {
	minRed, minGreen, minBlue := 0, 0, 0

	for _, round := range g.rounds {
		if round.red > minRed {
			minRed = round.red
		}

		if round.green > minGreen {
			minGreen = round.green
		}

		if round.blue > minBlue {
			minBlue = round.blue
		}
	}

	return []int{minRed, minGreen, minBlue}
}

type Round struct {
	red   int
	green int
	blue  int
}

func (r Round) IsPossible(red int, green int, blue int) bool {
	return (r.red <= red) && (r.green <= green) && (r.blue <= blue)
}

type Day2 struct {
	games []Game
}

func (d Day2) Part1() int {
	minRed, minGreen, minBlue := 12, 13, 14

	idTotal := 0
	for _, game := range d.games {
		if game.IsPossible(minRed, minGreen, minBlue) {
			idTotal += game.id
		}
	}

	return idTotal
}

func (d Day2) Part2() int {
	var minimums [][]int
	sumOfPowers := 0

	for _, game := range d.games {
		minimums = append(minimums, game.MinNeeded())
	}

	for _, mins := range minimums {
		sumOfPowers += mins[0] * mins[1] * mins[2]
	}

	return sumOfPowers
}

func CreateRound(roundInputStr string) Round {
	tokens := strings.Split(roundInputStr, ",")
	red, green, blue := 0, 0, 0

	for _, token := range tokens {
		pair := strings.Split(strings.TrimSpace(token), " ")
		switch pair[1] {
		case "red":
			red, _ = strconv.Atoi(pair[0])
		case "green":
			green, _ = strconv.Atoi(pair[0])
		case "blue":
			blue, _ = strconv.Atoi(pair[0])
		}
	}

	return Round{red, green, blue}
}

func CreateGame(gameLine string) Game {
	tokens := strings.Split(gameLine, ":")
	id, _ := strconv.Atoi(strings.Split(strings.TrimSpace(tokens[0]), " ")[1])
	var rounds []Round

	for _, round_str := range strings.Split(tokens[1], ";") {
		rounds = append(rounds, CreateRound(round_str))
	}

	return Game{id: id, rounds: rounds}
}

func CreateDay2(lines []string) Day2 {
	var games []Game
	for _, line := range lines {
		games = append(games, CreateGame(line))
	}

	return Day2{games}
}

func main() {
	day_2 := CreateDay2(internal.ReadPuzzleInput("./input/day2.txt"))
	fmt.Println("Part 1 total:", day_2.Part1())
	fmt.Println("Part 2 total:", day_2.Part2())
}

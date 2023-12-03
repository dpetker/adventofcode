// Day 2 - Now in Go!
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Game struct {
	id     int
	rounds []Round
}

func (g Game) is_possible(red int, green int, blue int) bool {
	for _, round := range g.rounds {
		if !round.is_possible(red, green, blue) {
			return false
		}
	}
	return true
}

func (g Game) min_needed() []int {
	min_red, min_green, min_blue := 0, 0, 0

	for _, round := range g.rounds {
		if round.red > min_red {
			min_red = round.red
		}

		if round.green > min_green {
			min_green = round.green
		}

		if round.blue > min_blue {
			min_blue = round.blue
		}
	}

	return []int{min_red, min_green, min_blue}
}

type Round struct {
	red   int
	green int
	blue  int
}

func (r Round) is_possible(red int, green int, blue int) bool {
	return (r.red <= red) && (r.green <= green) && (r.blue <= blue)
}

type Day2 struct {
	games []Game
}

func (d Day2) part_1() int {
	min_red, min_green, min_blue := 12, 13, 14

	id_total := 0
	for _, game := range d.games {
		if game.is_possible(min_red, min_green, min_blue) {
			id_total += game.id
		}
	}

	return id_total
}

func (d Day2) part_2() int {
	var minimums [][]int
	sum_of_powers := 0

	for _, game := range d.games {
		minimums = append(minimums, game.min_needed())
	}

	for _, mins := range minimums {
		sum_of_powers += mins[0] * mins[1] * mins[2]
	}

	return sum_of_powers
}

func create_round(round_input_str string) Round {
	tokens := strings.Split(round_input_str, ",")
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

func create_game(game_line string) Game {
	tokens := strings.Split(game_line, ":")
	id, _ := strconv.Atoi(strings.Split(strings.TrimSpace(tokens[0]), " ")[1])
	var rounds []Round

	for _, round_str := range strings.Split(tokens[1], ";") {
		rounds = append(rounds, create_round(round_str))
	}

	return Game{id: id, rounds: rounds}
}

func create_day_2(lines []string) Day2 {
	var games []Game
	for _, line := range lines {
		games = append(games, create_game(line))
	}

	return Day2{games}
}

func main() {
	file, err := os.Open("./input/day2.txt")

	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	day_2 := create_day_2(lines)
	fmt.Println("Part 1 total:", day_2.part_1())
	fmt.Println("Part 2 total:", day_2.part_2())
}

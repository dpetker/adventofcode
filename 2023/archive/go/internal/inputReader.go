package internal

import (
	"bufio"
	"log"
	"os"
)

// inputReader.go - utilities for loading puzzle input
func ReadPuzzleInput(filePath string) []string {
	file, err := os.Open(filePath)

	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}

# Solution for Day 2 of Advent of Code 2018
# Problem description: https://adventofcode.com/2018/day/2

import os

def calculate_checksum(boxes):
  num_twos = 0
  num_threes = 0

  for box in boxes:
    seen_letters = {}

    for letter in box:
      if letter not in seen_letters:
        seen_letters[letter] = 0

      seen_letters[letter] += 1

    seen_freqs = set(seen_letters.values())

    if 2 in seen_freqs:
      num_twos += 1

    if 3 in seen_freqs:
      num_threes += 1

  return num_twos * num_threes

if __name__ == '__main__':
  with open(os.path.join(os.path.dirname(__file__), '../input/day2.txt'), 'r') as f:
    lines = f.readlines()
    day2_input = [line.strip() for line in lines]

  checksum = calculate_checksum(day2_input)
  # common_id =

  print(f"Checksum is: {checksum}")


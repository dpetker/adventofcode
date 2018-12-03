# Solution for Day 1 of Advent of Code 2018
# Problem description: https://adventofcode.com/2018/day/1

import os

def calculate_frequency(change_list, current_freq, seen_freqs):
  duplicate_freq = None

  for number in change_list:
    current_freq += number

    if (current_freq in seen_freqs) and (duplicate_freq is None):
      duplicate_freq = current_freq

    seen_freqs.add(current_freq)

  return (current_freq, seen_freqs, duplicate_freq)

if __name__ == '__main__':
  with open(os.path.join(os.path.dirname(__file__), '../input/day1.txt'), 'r') as f:
    lines = f.readlines()
    day1_input = [int(line.strip()) for line in lines]

  current_freq, seen_freqs, duplicate_freq = calculate_frequency(day1_input, 0, set())
  result_freq = current_freq

  while duplicate_freq is None:
    current_freq, seen_freqs, duplicate_freq = calculate_frequency(day1_input, current_freq, seen_freqs)

  print(f"Resulting Frequency is: {result_freq}")
  print(f"First duplicate Frequency is: {duplicate_freq}")


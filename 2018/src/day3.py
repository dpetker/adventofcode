# Solution for Day 3 of Advent of Code 2018
# Problem description: https://adventofcode.com/2018/day/3

import os

class Claim:
  def __init__(self, data):
    tokens = data.split()

    # Strip the pound sign out
    self.id = int(tokens[0][1:])

    offset_tokens = tokens[2].split(",")
    self.offset_left = int(offset_tokens[0])
    self.offset_top = int(offset_tokens[1][:-1])

    dimension_tokens = tokens[3].split("x")
    self.width = int(dimension_tokens[0])
    self.height = int(dimension_tokens[1])

  def __str__(self):
    return f"#{self.id} @ {self.offset_left},{self.offset_top}: {self.width}x{self.height}"

def calculate_checksum(boxes):
  return None

if __name__ == '__main__':
  with open(os.path.join(os.path.dirname(__file__), '../input/day3.txt'), 'r') as f:
    lines = f.readlines()
    day3_input = [Claim(line.strip()) for line in lines]

  print(day3_input[0])


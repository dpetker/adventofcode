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

class Fabric:
  def __init__(self, initial_size = 2):
    self.plane = []

    for i in range(initial_size):
      self.plane.append(["."] * initial_size)

    # We'll calculate this as we apply claims
    self.num_overlapping_inches = 0

  def apply_claims(self, claims):
    for claim in claims:
      width_required = claim.offset_left + claim.width
      height_required = claim.offset_top + claim.height

      current_width = len(self.plane[0])
      current_height = len(self.plane)

      if (width_required > current_width) or (height_required > current_height):
        num_new_cols = width_required - current_width
        num_new_rows = height_required - current_height
        self.extend_plane(num_new_rows, num_new_cols)

      self.__apply_claim(claim)

  def extend_plane(self, new_rows, new_cols):
    current_width = len(self.plane[0])

    # Start by adding more rows, if needed
    if new_rows > 0:
      for i in range(new_rows):
        self.plane.append(["."] * current_width)

    # Add more columns, if needed
    if new_cols > 0:
      for row in self.plane:
        for i in range(new_cols):
          row.append(".")

  def __apply_claim(self, claim):
    affected_rows = self.plane[claim.offset_top : claim.offset_top + claim.height]

    for row in affected_rows:
      for col in range(claim.offset_left, claim.offset_left + claim.width):
        if row[col] != ".":
          if row[col] != "x":
            row[col] = "x"
            self.num_overlapping_inches += 1
        else:
          row[col] = str(claim.id)

  def __str__(self):
    result = ""
    for row in self.plane:
      result += " ".join(row)
      result += "\n"

    return result

if __name__ == '__main__':
  with open(os.path.join(os.path.dirname(__file__), '../input/day3.txt'), 'r') as f:
    lines = f.readlines()
    day3_input = [Claim(line.strip()) for line in lines]

  # Problem description says we'll start with at least 1000x1000
  fabric = Fabric(1000)
  fabric.apply_claims(day3_input)

  print(f"The number of overlapping square inches is: {fabric.num_overlapping_inches}")

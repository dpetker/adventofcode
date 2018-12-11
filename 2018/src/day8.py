# Solution for Day 8 of Advent of Code 2018
# Problem description: https://adventofcode.com/2018/day/8

class Node:
  def __init__(self):
    self.children = []
    self.metadata = []

  def metadata_sum(self):
    result = 0
    for child in self.children:
      result += child.metadata_sum()

    result += sum(self.metadata)

  def __str__(self):
    result = f"{len(self.children)} {len(self.metadata)} "

    for child in self.children:
      result += str(child)

    result += " ".join([str(m) for m in self.metadata])

    return result.strip()

def create_node_tree(input):
  entries = [int(num) for num in input.split()]

  root = Node()
  num_children = entries[0]
  num_metadata = entries[1]

  metadata_index = -1 * num_metadata

  root.metadata = entries[metadata_index:]
  root.children = [Node() for i in range(num_children)]

  if num_children == 0:
    return root

  remaining_entries = entries[2:metadata_index]

  return root

if __name__ == '__main__':
  print("Please run this via unittest:\n$ python -m unittest -f test/test_day8.py")

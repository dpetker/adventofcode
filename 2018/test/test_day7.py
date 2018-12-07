import unittest
import os
from src.day7 import find_path

class TestReactPolymer(unittest.TestCase):
  def test_sample_input(self):
    sample_data = [
      "Step C must be finished before step A can begin.",
      "Step C must be finished before step F can begin.",
      "Step A must be finished before step B can begin.",
      "Step A must be finished before step D can begin.",
      "Step B must be finished before step E can begin.",
      "Step D must be finished before step E can begin.",
      "Step F must be finished before step E can begin."
    ]

    self.assertEqual(find_path(sample_data), "CABDFE")

  def test_real_input_part_one(self):
    with open(os.path.join(os.path.dirname(__file__), '../input/day7.txt'), 'r') as f:
      lines = f.readlines()
      day7_input = [line.strip() for line in lines]

    result = find_path(day7_input)
    print(f"The correct order of steps is {result}")
    self.assertEqual(result, "BDHNEGOLQASVWYPXUMZJIKRTFC")

if __name__ == '__main__':
  unittest.main()

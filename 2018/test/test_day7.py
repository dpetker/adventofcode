import unittest
import os
from src.day7 import find_basic_path, find_path_in_parallel

SAMPLE_DATA = [
  "Step C must be finished before step A can begin.",
  "Step C must be finished before step F can begin.",
  "Step A must be finished before step B can begin.",
  "Step A must be finished before step D can begin.",
  "Step B must be finished before step E can begin.",
  "Step D must be finished before step E can begin.",
  "Step F must be finished before step E can begin."
]

class TestAssemblyInstructions(unittest.TestCase):
  def test_sample_input_part_one(self):
    self.assertEqual(find_basic_path(SAMPLE_DATA), "CABDFE")

  def test_real_input_part_one(self):
    with open(os.path.join(os.path.dirname(__file__), '../input/day7.txt'), 'r') as f:
      lines = f.readlines()
      day7_input = [line.strip() for line in lines]

    result = find_basic_path(day7_input)
    print(f"The correct order of steps for Part One is {result}")
    self.assertEqual(result, "BDHNEGOLQASVWYPXUMZJIKRTFC")

  def test_sample_input_part_two(self):
    result, total_time = find_path_in_parallel(SAMPLE_DATA, 2, 0)
    self.assertEqual(result, "CABFDE")
    self.assertEqual(total_time, 15)

  def test_real_input_part_two(self):
    with open(os.path.join(os.path.dirname(__file__), '../input/day7.txt'), 'r') as f:
      lines = f.readlines()
      day7_input = [line.strip() for line in lines]

    result, total_time = find_path_in_parallel(day7_input, 5, 60)
    print(f"The total time for Part Two is {total_time}s")
    self.assertEqual(total_time, 1107)

if __name__ == '__main__':
  unittest.main()

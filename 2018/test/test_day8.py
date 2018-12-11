import unittest
import os
from src.day8 import create_node_tree

SAMPLE_DATA = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

class TestMemoryManeuver(unittest.TestCase):
  def test_sample_input_part_one(self):
    tree = create_node_tree(SAMPLE_DATA)
    self.assertEqual(str(tree), SAMPLE_DATA)
    self.assertEqual(tree.metadata_sum, 138)

  # def test_real_input_part_one(self):
  #   with open(os.path.join(os.path.dirname(__file__), '../input/day7.txt'), 'r') as f:
  #     lines = f.readlines()
  #     day7_input = [line.strip() for line in lines]

  #   result = find_basic_path(day7_input)
  #   print(f"The correct order of steps for Part One is {result}")
  #   self.assertEqual(result, "BDHNEGOLQASVWYPXUMZJIKRTFC")

  # def test_sample_input_part_two(self):
  #   result, total_time = find_path_in_parallel(SAMPLE_DATA, 2, 0)
  #   self.assertEqual(result, "CABFDE")
  #   self.assertEqual(total_time, 15)

  # def test_real_input_part_two(self):
  #   with open(os.path.join(os.path.dirname(__file__), '../input/day7.txt'), 'r') as f:
  #     lines = f.readlines()
  #     day7_input = [line.strip() for line in lines]

  #   result, total_time = find_path_in_parallel(day7_input, 5, 60)
  #   print(f"The total time for Part Two is {total_time}s")
  #   self.assertEqual(total_time, 1107)

if __name__ == '__main__':
  unittest.main()

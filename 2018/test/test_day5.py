import unittest
import os
from src.day5 import react_polymer, improve_polymer

class TestReactPolymer(unittest.TestCase):
  def test_sample_input(self):
    sample_data = "dabAcCaCBAcCcaDA"
    expected_data = "dabCBAcaDA"
    result = react_polymer(sample_data)

    self.assertEqual(result, expected_data)

  def test_full_destruction(self):
    self.assertEqual(react_polymer("abBA"), "")

  def test_recursive_destruction(self):
    self.assertEqual(react_polymer("zabcdefgGFEDCBAz"), "zz")

  def test_real_input_part_one(self):
    self.skipTest("Takes too long during development")
    with open(os.path.join(os.path.dirname(__file__), '../input/day5.txt'), 'r') as f:
      lines = f.readlines()
      day5_input = lines[0].strip()

    result = react_polymer(day5_input)
    print(f"The length of polymer remaining is: {len(result)} units.")
    self.assertEqual(len(result), 11668)

class TestImprovePolymer(unittest.TestCase):
  def test_sample_input(self):
    sample_data = "dabAcCaCBAcCcaDA"
    expected_data = "daDA"
    result = improve_polymer(sample_data)

    self.assertEqual(result, expected_data)

  def test_real_input_part_two(self):
    with open(os.path.join(os.path.dirname(__file__), '../input/day5.txt'), 'r') as f:
      lines = f.readlines()
      day5_input = lines[0].strip()

    result = improve_polymer(day5_input)
    print(f"The length of polymer remaining is: {len(result)} units.")
    # self.assertEqual(len(result), 11668)

if __name__ == '__main__':
  unittest.main()

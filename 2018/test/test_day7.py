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

if __name__ == '__main__':
  unittest.main()

# Solution for Day 4 of Advent of Code 2018
# Problem description: https://adventofcode.com/2018/day/4

import os
from datetime import datetime

class Record:
  def __init__(self, line):
    tokens = line.split(']')

    self.date = datetime.strptime(tokens[0][1:], "%Y-%m-%d %H:%M")

    action = tokens[1].strip()
    if action.startswith("Guard"):
      self.type = "guard"
      action_tokens = action.split()
      self.guard_id = int(action_tokens[1][1:])
    elif action.startswith("falls"):
      self.type = "asleep"
    else:
      self.type = "wakes"

  def __str__(self):
    result = f"[{self.date.strftime('%Y-%m-%d %H:%M')}] "

    if self.type == "guard":
      result += f"Guard #{self.guard_id} begins shift"
    elif self.type == 'asleep':
      result += "falls asleep"
    else:
      result += "wakes up"

    return result


if __name__ == '__main__':
  # with open(os.path.join(os.path.dirname(__file__), '../input/day4.txt'), 'r') as f:
  #   lines = f.readlines()
  #   day4_input = [Record(line.strip()) for line in lines]

  sample_data = [
    "[1518-11-01 00:00] Guard #10 begins shift",
    "[1518-11-01 00:05] falls asleep",
    "[1518-11-01 00:25] wakes up",
    "[1518-11-01 00:30] falls asleep",
    "[1518-11-01 00:55] wakes up",
    "[1518-11-01 23:58] Guard #99 begins shift",
    "[1518-11-02 00:40] falls asleep",
    "[1518-11-02 00:50] wakes up",
    "[1518-11-03 00:05] Guard #10 begins shift",
    "[1518-11-03 00:24] falls asleep",
    "[1518-11-03 00:29] wakes up",
    "[1518-11-04 00:02] Guard #99 begins shift",
    "[1518-11-04 00:36] falls asleep",
    "[1518-11-04 00:46] wakes up",
    "[1518-11-05 00:03] Guard #99 begins shift",
    "[1518-11-05 00:45] falls asleep",
    "[1518-11-05 00:55] wakes up"
  ]
  sample_data.reverse()

  day4_input = [Record(datum) for datum in sample_data]
  day4_input.sort(key = lambda record: record.date)
  for day in day4_input:
    print(day)

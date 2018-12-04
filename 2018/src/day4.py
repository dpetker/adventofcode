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

class CombinedRecord:
  def __init__(self, records):
    self.guard_id = records[0].guard_id
    self.did_not_sleep = False
    self.sleep_tuples = []

    if len(records) == 1:
      # Special case, did not sleep
      self.did_not_sleep = True
      self.month = records[0].date.month
      self.day = records[0].date.day if records[0].date.minute == 0 else records[0].date.day + 1
      return

    self.month = records[1].date.month
    self.day = records[1].date.day

    for i in range(1, len(records), 2):
      self.sleep_tuples.append((records[i].date.minute, records[i + 1].date.minute))

  def is_asleep(self, minute):
    if self.did_not_sleep:
      return False

    for sleepy_time in self.sleep_tuples:
      if minute >= sleepy_time[0] and minute < sleepy_time[1]:
        return True

    return False

  def __str__(self):
    formatted_month = self.month if self.month > 9 else f"0{self.month}"
    formatted_day = self.day if self.day > 9 else f"0{self.day}"
    formatted_guard_id = f"#{self.guard_id}"

    num_spaces = 5 - len(formatted_guard_id)
    formatted_guard_id += " " * num_spaces

    result = f"{formatted_month}-{formatted_day}  {formatted_guard_id}  "

    for i in range(60):
      if self.is_asleep(i):
        result += "#"
      else:
        result += "."

    return result + "\n"

class GuardHistogram:
  def __init__(self, combined_records):
    self.data = [0] * 60

    for record in combined_records:
      for i in range(60):
        if record.is_asleep(i):
          self.data[i] += 1

  def max_tuple(self):
    max_value = max(self.data)
    max_index = self.data.index(max_value)
    return (max_value, max_index)

  def most_likely_minute(self):
    return self.max_tuple()[1]

  def total_minutes_slept(self):
    return sum(self.data)

class Schedule:
  def __init__(self, records):
    self.records = records
    self.records.sort(key = lambda record: record.date)
    self.unique_guard_ids = set()

    self.combined_records = self.__combine_records(self.records)
    self.guard_histogram = self.__create_histogram_by_guard(self.combined_records, self.unique_guard_ids)

  def show_histogram(self):
    for guard_id, histogram in self.guard_histogram.items():
      print(f"#{guard_id} {histogram.data}")

  def find_max_chance_part_one(self):
    current_total_min_slept = 0
    current_histogram = None
    current_guard_id = None

    for guard_id, histogram in self.guard_histogram.items():
      if histogram.total_minutes_slept() > current_total_min_slept:
        current_total_min_slept = histogram.total_minutes_slept()
        current_histogram = histogram
        current_guard_id = guard_id

    return (current_guard_id, current_histogram.most_likely_minute())

  def find_max_chance_part_two(self):
    current_max_tuple = (0, 0)
    current_guard_id = None

    for guard_id, histogram in self.guard_histogram.items():
      check_tuple = histogram.max_tuple()

      if check_tuple[0] > current_max_tuple[0]:
        current_max_tuple = check_tuple
        current_guard_id = guard_id

    return (current_guard_id, current_max_tuple[1])

  def __combine_records(self, records):
    combined_records = []

    guard_indices = [i for i, record in enumerate(records) if record.type == "guard"]
    prev_index = None
    slices = []
    for index in guard_indices:
      if prev_index is not None:
        slices.append(records[prev_index:index])

      prev_index = index

    slices.append(records[prev_index:])

    for s in slices:
      cr = CombinedRecord(s)
      combined_records.append(cr)
      self.unique_guard_ids.add(cr.guard_id)

    return combined_records

  def __create_histogram_by_guard(self, combined_records, unique_guard_ids):
    histogram = {}
    for guard_id in unique_guard_ids:
      relevant_records = []
      for cr in combined_records:
        if cr.guard_id == guard_id:
          relevant_records.append(cr)

      histogram[guard_id] = GuardHistogram(relevant_records)

    return histogram

  def __str__(self):
    result = "Date   ID     Minute\n"
    result += "              000000000011111111112222222222333333333344444444445555555555\n"
    result += "              012345678901234567890123456789012345678901234567890123456789\n"

    for cr in self.combined_records:
      result += str(cr)

    return result

if __name__ == '__main__':
  with open(os.path.join(os.path.dirname(__file__), '../input/day4.txt'), 'r') as f:
    lines = f.readlines()
    day4_input = [Record(line.strip()) for line in lines]

  schedule = Schedule(day4_input)
  solution_part_one = schedule.find_max_chance_part_one()
  solution_part_two = schedule.find_max_chance_part_two()

  print(f"Your best chance for Part One is #{solution_part_one[0]} at minute {solution_part_one[1]} (Or, {solution_part_one[0] * solution_part_one[1]})")
  print(f"Your best chance for Part Two is #{solution_part_two[0]} at minute {solution_part_two[1]} (Or, {solution_part_two[0] * solution_part_two[1]})")

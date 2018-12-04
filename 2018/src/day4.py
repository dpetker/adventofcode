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

class Schedule:
  def __init__(self, records):
    self.records = records
    self.records.sort(key = lambda record: record.date)

    self.combined_records = self.__combine_records(self.records)

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
      combined_records.append(CombinedRecord(s))

    return combined_records

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

  # sample_data = [
  #   "[1518-11-01 00:00] Guard #10 begins shift",
  #   "[1518-11-01 00:05] falls asleep",
  #   "[1518-11-01 00:25] wakes up",
  #   "[1518-11-01 00:30] falls asleep",
  #   "[1518-11-01 00:55] wakes up",
  #   "[1518-11-01 23:58] Guard #99 begins shift",
  #   "[1518-11-02 00:40] falls asleep",
  #   "[1518-11-02 00:50] wakes up",
  #   "[1518-11-03 00:05] Guard #10 begins shift",
  #   "[1518-11-03 00:24] falls asleep",
  #   "[1518-11-03 00:29] wakes up",
  #   "[1518-11-04 00:02] Guard #99 begins shift",
  #   "[1518-11-04 00:36] falls asleep",
  #   "[1518-11-04 00:46] wakes up",
  #   "[1518-11-05 00:03] Guard #99 begins shift",
  #   "[1518-11-05 00:45] falls asleep",
  #   "[1518-11-05 00:55] wakes up"
  # ]
  # sample_data.reverse()

  # day4_input = [Record(datum) for datum in sample_data]

  schedule = Schedule(day4_input)

  print(schedule)

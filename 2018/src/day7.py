# Solution for Day 7 of Advent of Code 2018
# Problem description: https://adventofcode.com/2018/day/7

class Step:
  def __init__(self, id):
    self.id = id
    self.prereqs = []
    self.is_complete = False

  def add_prereq(self, prereq):
    self.prereqs.append(prereq)

  def can_complete(self):
    for prereq in self.prereqs:
      if not prereq.is_complete:
        return False

    return True

  def __str__(self):
    return f"{self.id}: {[p.id for p in self.prereqs]}"

class AssemblyInstructions:
  def __init__(self):
    self.steps = {}

  def step_for(self, id):
    if id not in self.steps:
      self.steps[id] = Step(id)

    return self.steps[id]

  def __str__(self):
    result = ""

    for id, step in self.steps.items():
      result += f"{step}\n"

    return result

def find_path(steps):
  ai = AssemblyInstructions()
  for step in steps:
    tokens = step.split()
    prereq = ai.step_for(tokens[1])
    step = ai.step_for(tokens[-3])

    step.add_prereq(prereq)

  incomplete_steps = list(ai.steps.keys())
  incomplete_steps.sort()

  complete_steps = []

  while incomplete_steps:
    for i in range(len(incomplete_steps)):
      test_step = ai.step_for(incomplete_steps[i])
      if test_step.can_complete():
        test_step.is_complete = True
        complete_steps.append(incomplete_steps.pop(i))
        break

  return "".join(complete_steps)

if __name__ == '__main__':
  print("Please run this via unittest:\n$ python -m unittest -f test/test_day7.py")

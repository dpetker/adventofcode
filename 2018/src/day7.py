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
    self.steps = []

  def step_for(self, id):
    for step in self.steps:
      if step.id == id:
        return step

    new_step = Step(id)
    self.steps.append(new_step)

    # Keep steps sorted by ID
    self.steps.sort(key = lambda step: step.id)

    return new_step

  def __str__(self):
    result = ""

    for id, step in self.steps.items():
      result += f"{step}\n"

    return result

def find_basic_path(steps):
  ai = AssemblyInstructions()
  for step in steps:
    tokens = step.split()
    prereq = ai.step_for(tokens[1])
    step = ai.step_for(tokens[-3])

    step.add_prereq(prereq)

  complete_steps = []

  while ai.steps:
    for i in range(len(ai.steps)):
      test_step = ai.steps[i]
      if test_step.can_complete():
        test_step.is_complete = True
        complete_steps.append(ai.steps.pop(i))
        break

  return "".join([s.id for s in complete_steps])

if __name__ == '__main__':
  print("Please run this via unittest:\n$ python -m unittest -f test/test_day7.py")

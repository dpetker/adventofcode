# Solution for Day 7 of Advent of Code 2018
# Problem description: https://adventofcode.com/2018/day/7

class Step:
  def __init__(self, id, time_offset = 0):
    self.id = id
    self.prereqs = []
    self.ticks_to_complete = time_offset + (ord(id) - 64)
    self.is_complete = False
    self.being_worked_on = False

  def add_prereq(self, prereq):
    self.prereqs.append(prereq)

  def prereqs_complete(self):
    for prereq in self.prereqs:
      if not prereq.is_complete:
        return False

    return True

  def __str__(self):
    return f"{self.id} ({self.ticks_to_complete}): {[p.id for p in self.prereqs]}"

class AssemblyInstructions:
  def __init__(self, time_offset = 0):
    self.steps = []
    self.time_offset = time_offset

  def step_for(self, id):
    for step in self.steps:
      if step.id == id:
        return step

    new_step = Step(id, self.time_offset)
    self.steps.append(new_step)

    # Keep steps sorted by ID
    self.steps.sort(key = lambda step: step.id)

    return new_step

  def __str__(self):
    result = "<AssemblyInstructions>\n"

    for step in self.steps:
      result += f"{step}\n"

    result += "</AssemblyInstructions>"
    return result

class Worker:
  def __init__(self, id):
    self.id = id
    self.work = None

  def has_work(self):
    return self.work is not None

  def work_complete(self):
    return self.has_work() and self.work.ticks_to_complete == 0

  def tick(self):
    if self.has_work() and self.work.ticks_to_complete > 0:
      self.work.ticks_to_complete -= 1

def __build_graph(steps, time_offset = 0):
  ai = AssemblyInstructions(time_offset)
  for step in steps:
    tokens = step.split()
    prereq = ai.step_for(tokens[1])
    step = ai.step_for(tokens[-3])

    step.add_prereq(prereq)

  return ai

def find_basic_path(steps):
  ai = __build_graph(steps)

  complete_steps = []
  ctr = 10000 # Just so we don't infinite loop

  while ai.steps and ctr > 0:
    for i in range(len(ai.steps)):
      test_step = ai.steps[i]
      if test_step.prereqs_complete():
        test_step.is_complete = True
        complete_steps.append(ai.steps.pop(i))
        break

    ctr -= 1

  return "".join([s.id for s in complete_steps])

def __handle_completed_work(worker):
  worker_step = worker.work
  worker.work = None
  worker_step.is_complete = True
  worker_step.being_worked_on = False

  return worker_step

def find_path_in_parallel(steps, num_workers, time_offset):
  ai = __build_graph(steps, time_offset)
  workers = [Worker(i) for i in range(num_workers)]

  complete_steps = []
  ctr = 10000 # Just so we don't infinite loop

  while ai.steps and ctr > 0:
    # Step 1: tick all our workers, and check if any are free (and any)
    # work needs to be added to completed_steps
    free_workers = []
    for worker in workers:
      worker.tick()
      if worker.work_complete():
        completed_work = __handle_completed_work(worker)
        complete_steps.append(completed_work)
        free_workers.append(worker)
      elif not worker.has_work():
        free_workers.append(worker)

    # Step 2: find all steps available to be worked on and assign to an
    # available worker (if possible)
    for freebie in free_workers:
      for i in range(len(ai.steps)):
        test_step = ai.steps[i]
        if test_step.prereqs_complete() and not test_step.being_worked_on:
          freebie.work = ai.steps.pop(i)
          freebie.work.being_worked_on = True
          break

    ctr -= 1

  # Final step: Drain any workers that are still in progress
  in_progress_workers = []
  for worker in workers:
    if worker.has_work():
      in_progress_workers.append(worker)

  while in_progress_workers:
    for i in range(len(in_progress_workers)):
      worker = in_progress_workers[i]
      worker.tick()
      if worker.work_complete():
        completed_work = __handle_completed_work(worker)
        complete_steps.append(completed_work)
        in_progress_workers.pop(i)
        break

  return "".join([s.id for s in complete_steps])

if __name__ == '__main__':
  print("Please run this via unittest:\n$ python -m unittest -f test/test_day7.py")

# Solution for Day 5 of Advent of Code 2018
# Problem description: https://adventofcode.com/2018/day/5

def test_pair(unit_one, unit_two):
  if (unit_one.isupper() and unit_two.isupper()) or (unit_one.islower() and unit_two.islower()):
    # Both same case, no match
    return False

  return unit_one.lower() == unit_two.lower()

def trigger_first_reaction(polymer):
  for i in range(len(polymer) - 1):
    if test_pair(polymer[i], polymer[i+1]):
      return (polymer[:i] + polymer[i+2:], True)

  # If we get here, no reaction occurred
  return (polymer, False)

def react_polymer(polymer):
  reaction_occurred = True
  while reaction_occurred:
    polymer, reaction_occurred = trigger_first_reaction(polymer)

  return polymer

def improve_polymer(polymer):
  unique_units = set(polymer.lower())
  shortest_result = polymer
  current_count = 0

  for unit in unique_units:
    current_count += 1

    print(f"Analyzing permutation {current_count}/{len(unique_units)}")

    test_polymer = polymer.replace(unit, "").replace(unit.upper(), "")
    result = react_polymer(test_polymer)

    if len(result) < len(shortest_result):
      shortest_result = result

  return shortest_result

if __name__ == '__main__':
  print("Please run this via unittest:\n$ python -m unittest -f test/test_day5.py")




# day1.rb - Day 1 solution, ruby-fied!

# Part 1
part_1_running_total = 0
File.open("./input/day1.txt").each do |line|
  if line[0] == "#"
    next
  end

  all_digits = line.scan(/\d/)
  part_1_running_total += "#{all_digits.first}#{all_digits.last}".to_i
end

puts "Part 1 total: #{part_1_running_total}"

# Part 2
part_2_running_total = 0
number_to_digit_hash = {
  'one' => 1,
  'two' => 2,
  'three' => 3,
  'four' => 4,
  'five' => 5,
  'six' => 6,
  'seven' => 7,
  'eight' => 8,
  'nine' => 9,
  '1' => 1,
  '2' => 2,
  '3' => 3,
  '4' => 4,
  '5' => 5,
  '6' => 6,
  '7' => 7,
  '8' => 8,
  '9' => 9
}
File.open("./input/day1.txt").each do |line|
  if line[0] == "#"
    next
  end

  all_digits = line.scan(/(?=(\d|one|two|three|four|five|six|seven|eight|nine))/).flatten
  part_2_running_total += "#{number_to_digit_hash[all_digits.first]}#{number_to_digit_hash[all_digits.last]}".to_i
end

puts "Part 2 total: #{part_2_running_total}" # Part 2 total: 54518

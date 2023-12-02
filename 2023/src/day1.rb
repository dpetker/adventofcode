# day1.rb - Day 1 solution, ruby-fied!
class Day1
  @@number_to_digit_hash = {
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

  def initialize(input_lines)
    @input_lines = input_lines
  end

  def part_1
    @input_lines.sum do |line|
      if line[0] == "#"
        next
      end

      all_digits = line.scan(/\d/)
      "#{all_digits.first}#{all_digits.last}".to_i
    end
  end

  def part_2
    @input_lines.sum do |line|
      if line[0] == "#"
        next
      end

      all_digits = line.scan(/(?=(\d|one|two|three|four|five|six|seven|eight|nine))/).flatten
      "#{@@number_to_digit_hash[all_digits.first]}#{@@number_to_digit_hash[all_digits.last]}".to_i
    end
  end
end

day_1 = Day1.new(IO.readlines("./input/day1.txt"))
puts "Part 1 total: #{day_1.part_1}" # Part 1 total: 54331
puts "Part 2 total: #{day_1.part_2}" # Part 2 total: 54518

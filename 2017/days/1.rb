# Part 1 of the CAPTCHA decode - comparing to previous digit
File.open("../inputs/1.txt").each do |line|
  if line[0] == "#"
    next
  end

  prev_digit = -1
  digit = -1
  sum = 0

  line.gsub("\n", "").split("").each do |char|
    digit = char.to_i

    if digit == prev_digit
      sum += digit
    end

    prev_digit = digit
  end

  # check if last digit matches first
  if digit == line[0].to_i
    sum += digit
  end

  puts "CAPTCHA part 1 decode complete! Your answer is: #{sum}."
end

# Part 2 of CAPTCHA decode - compare to halfway around
File.open("../inputs/1.txt").each do |line|
  if line[0] == "#"
    next
  end

  line = line.gsub("\n", "")

  size = line.size
  halfway = size / 2
  sum = 0

  line.split("").each_with_index do |char, index|
    digit = char.to_i
    halfway_index = (index + halfway) % size
    halfway_digit = line[halfway_index].to_i

    if digit == halfway_digit
      sum += digit
    end
  end

  puts "CAPTCHA part 2 decode complete! Your answer is: #{sum}."
end

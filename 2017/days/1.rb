File.open("../inputs/1.txt").each do |line|
  prev_digit = -1
  digit = -1
  sum = 0

  if line[0] == "#"
    next
  end

  line.split("").each do |char|
    if char == "\n"
      next
    end

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

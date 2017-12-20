# Day 2, Part 1 - Checksum
File.open("../inputs/2.txt").each do |line|
  if line[0] == "#"
    next
  end

  # lowest

  # line.gsub("\n", "").split("").each do |char|
    # digit = char.to_i

    # if digit == prev_digit
    #   sum += digit
    # end

    # prev_digit = digit
  # end

  # check if last digit matches first
  # if digit == line[0].to_i
  #   sum += digit
  # end

  # puts "CAPTCHA part 1 decode complete! Your answer is: #{sum}."
end

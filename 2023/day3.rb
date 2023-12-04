class Day3
  def initialize(use_sample_data=false)
    data_path = use_sample_data ? './input/day3_sample.txt' : './input/day3.txt'
    @data = IO.readlines(data_path)
  end

  def part_1
    Engine.new(@data).find_connected_parts.sum do |part|
      part.to_i
    end
  end

  def part_2
  end
end

class Engine
  def initialize(raw_schematic)
    # This processing came from a solution on reddit that helped me wrap my
    # head around the whole "a 3-digit number takes up 3 spaces" thing. This is
    # pretty ingenious: just repeat the 3-digit number 3 times which helps find
    # connected symbols, etc.
    @schematic = raw_schematic.each_with_object([]) do |line, matrix|
      nums = line.scan(/(?:\d+|.)/)

      matrix << nums.each_with_object([]) do |num, row|
        num.length.times { |_| row << num }
        row
      end

      matrix
    end
  end

  def find_connected_parts
    accum = []
    @schematic.each_with_index do |row, row_index|
      row.each_with_index do |piece, col_index|
        next if not piece.scan(/^\d+$/).first

        accum << piece if has_connection?(row_index, col_index)
      end
    end

    accum
  end

  def has_connection?(row, col)
    false
  end

  private :has_connection?
end

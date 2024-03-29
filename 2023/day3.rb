require 'set'

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
    Engine.new(@data).find_gear_ratios.sum
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
        num_repeats = num.length
        if num.scan(/^\d+$/).first
          num = Part.new(num)
        end

        num_repeats.times { |_| row << num }
        row
      end

      matrix
    end
  end

  def find_connected_parts
    accum = Set[]
    @schematic.each_with_index do |row, row_index|
      row.each_with_index do |piece, col_index|
        next if not piece.instance_of? Part

        accum << piece if has_connection?(row_index, col_index)
      end
    end

    accum
  end

  def find_gear_ratios
    accum = []

    @schematic.each_with_index do |row, row_index|
      row.each_with_index do |piece, col_index|
        next if not piece == "*"

        connected_parts = get_parts_connected_to_gear(row_index, col_index).to_a

        if connected_parts.length == 2
          accum << connected_parts[0].to_i * connected_parts[1].to_i
        end
      end
    end

    accum
  end

  def has_connection?(row, col)
    # top-left
    return true if is_symbol?(row - 1, col - 1)

    # top
    return true if is_symbol?(row - 1, col)

    # top-right
    return true if is_symbol?(row - 1, col + 1)

    # right
    return true if is_symbol?(row, col + 1)

    # bottom-right
    return true if is_symbol?(row + 1, col + 1)

    # bottom
    return true if is_symbol?(row + 1, col)

    # bottom-left
    return true if is_symbol?(row + 1, col - 1)

    # left
    return true if is_symbol?(row, col - 1)

    return false
  end

  def get_parts_connected_to_gear(row, col)
    accum = Set[]

    # top-left
    accum << @schematic[row - 1][col -1] if is_part?(row - 1, col - 1)

    # top
    accum << @schematic[row - 1][col] if is_part?(row - 1, col)

    # top-right
    accum << @schematic[row - 1][col + 1] if is_part?(row - 1, col + 1)

    # right
    accum << @schematic[row][col + 1] if is_part?(row, col + 1)

    # bottom-right
    accum << @schematic[row + 1][col + 1] if is_part?(row + 1, col + 1)

    # bottom
    accum << @schematic[row + 1][col] if is_part?(row + 1, col)

    # bottom-left
    accum << @schematic[row + 1][col - 1] if is_part?(row + 1, col - 1)

    # left
    accum << @schematic[row][col - 1] if is_part?(row, col - 1)

    accum
  end

  def is_symbol?(row, col)
    return false if row >= @schematic[0].length
    return false if col >= @schematic.length

    value = @schematic[row][col]

    return false if value.instance_of? Part

    return value.scan(/[^\d|^\.]/).length > 0
  end

  def is_part?(row, col)
    return false if row >= @schematic[0].length
    return false if col >= @schematic.length

    value = @schematic[row][col]

    return value.instance_of? Part
  end

  private :has_connection?, :is_symbol?, :is_part?
end

class Part
  def initialize(part_str)
    @id = part_str.to_i
  end

  def to_i
    @id
  end
end

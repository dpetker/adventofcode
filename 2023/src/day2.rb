class Game
  attr_reader :id
  attr_reader :rounds

  def initialize(game_line)
    tokens = game_line.split(':')
    @id = tokens[0].sub('Game ', '').to_i
    @rounds = tokens[1].split(';').map {|token| Round.new(token.strip)}
  end

  def possible?(red, green, blue)
    @rounds.each do |round|
      return false if not round.possible?(red, green, blue)
    end

    true
  end

  def min_needed
    min_red = 0
    min_green = 0
    min_blue = 0

    @rounds.each do |round|
      min_red = round.red if round.red > min_red
      min_green = round.green if round.green > min_green
      min_blue = round.blue if round.blue > min_blue
    end

    [min_red, min_green, min_blue]
  end
end

class Round
  attr_reader :red
  attr_reader :green
  attr_reader :blue

  def initialize(round_input_str)
    @red = 0
    @green = 0
    @blue = 0

    round_input_str.split(',').each do |token|
      pair = token.strip.split(' ')
      case pair[1]
      when 'red'
        @red = pair[0].to_i
      when 'green'
        @green = pair[0].to_i
      when 'blue'
        @blue = pair[0].to_i
      end
    end
  end

  def possible?(red, green, blue)
    (@red <= red) && (@green <= green) && (@blue <= blue)
  end
end


class Day2
  def initialize(input_lines)
    @games = input_lines.map {|line| Game.new(line)}
  end

  def part_1
    max_red = 12
    max_green = 13
    max_blue = 14

    @games.sum {|game| game.possible?(max_red, max_green, max_blue) ? game.id : 0}
  end

  def part_2
    minimums = @games.map {|game| game.min_needed}
    minimums.sum {|arr| arr[0] * arr[1] * arr[2]}
  end
end

day_2 = Day2.new(IO.readlines('./input/day2.txt'))
puts "Part 1 total: #{day_2.part_1}"
puts "Part 2 total: #{day_2.part_2}"

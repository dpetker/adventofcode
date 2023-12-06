class Day4
  def initialize(use_sample_data=false)
    data_path = use_sample_data ? './input/day4_sample.txt' : './input/day4.txt'
    @data = IO.readlines(data_path)
    @cards = @data.map {|line| Card.new(line)}
    @deck = Deck.new(@cards)
  end

  def part_1
    @cards.sum {|card| card.points}
  end

  def part_2
    @deck.add_copies.num_cards
  end
end

class Card
  attr_reader :id

  def initialize(data_line)
    tokens = data_line.split(':')
    @id = tokens[0].sub('Card', '').strip.to_i
    winning_str, have_str = tokens[1].split('|')

    @winning_vals = winning_str.split(' ').map {|e| e.to_i}
    @have_vals = have_str.split(' ').map {|e| e.to_i}
  end

  def points
    match_count = num_matches
    return 0 if match_count == 0

    2**(match_count - 1)
  end

  def num_matches
    @have_vals.intersection(@winning_vals).length
  end
end

class Deck
  def initialize(cards)
    @cards = cards
    @card_map = Hash.new

    @cards.each {|card| @card_map[card.id] = [card, 1]}
  end

  def num_cards
    @card_map.values.sum {|card_pair| card_pair[1]}
  end

  def add_copies
    @cards.each do |card|
      num_wins = card.num_matches
      current_count = @card_map[card.id][1]

      current_index = card.id
      num_wins.times do
        current_index += 1
        @card_map[current_index][1] += current_count
      end
    end

    self
  end
end

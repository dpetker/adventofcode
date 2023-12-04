require_relative "../day2"

describe Day2 do
  describe "part_1" do
    it "should come up with 2600" do
      d2 = Day2.new
      expect(d2.part_1).to eq(2600)
    end
  end

  describe "part_2" do
    it "should come up with 86036" do
      d2 = Day2.new
      expect(d2.part_2).to eq(86036)
    end
  end
end

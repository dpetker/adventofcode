require_relative "../day3"

describe Day3 do
  describe "(sample data)" do
    describe "part_1" do
      it "should come up with 4361" do
        d3 = Day3.new(use_sample_data=true)
        expect(d3.part_1).to eq(4361)
      end
    end

    describe "part_2" do
      it "should come up with 467835" do
        d3 = Day3.new(use_sample_data=true)
        expect(d3.part_2).to eq(467835)
      end
    end
  end

  describe "(actual data)" do
    describe "part_1" do
      it "should come up with 530495" do
        d3 = Day3.new()
        expect(d3.part_1).to eq(530495)
      end
    end

    describe "part_2" do
      it "should come up with 80253814" do
        d3 = Day3.new()
        expect(d3.part_2).to eq(80253814)
      end
    end
  end
end

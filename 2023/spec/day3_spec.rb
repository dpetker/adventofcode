require_relative "../day3"

describe Day3 do
  describe "(sample data)" do
    describe "part_1" do
      it "should come up with 4361" do
        d3 = Day3.new(use_sample_data=true)
        expect(d3.part_1).to eq(4361)
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
  end
end

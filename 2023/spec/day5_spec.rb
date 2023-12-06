require_relative "../day5"

describe Day5 do
  describe "(sample data)" do
    describe "part_1" do
      it "should come up with nil" do
        d5 = Day5.new(use_sample_data=true)
        expect(d5.part_1).to eq(nil)
      end
    end

    describe "part_2" do
      it "should come up with nil" do
        d5 = Day5.new(use_sample_data=true)
        expect(d5.part_2).to eq(nil)
      end
    end
  end

  describe "(actual data)" do
    describe "part_1" do
      it "should come up with nil" do
        d5 = Day5.new()
        expect(d5.part_1).to eq(nil)
      end
    end

    describe "part_2" do
      it "should come up with nil" do
        d5 = Day5.new()
        expect(d5.part_2).to eq(nil)
      end
    end
  end
end

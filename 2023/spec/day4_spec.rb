require_relative "../day4"

describe Day4 do
  describe "(sample data)" do
    describe "part_1" do
      it "should come up with 13" do
        d4 = Day4.new(use_sample_data=true)
        expect(d4.part_1).to eq(13)
      end
    end

    describe "part_2" do
      it "should come up with 30" do
        d4 = Day4.new(use_sample_data=true)
        expect(d4.part_2).to eq(30)
      end
    end
  end

  describe "(actual data)" do
    describe "part_1" do
      it "should come up with 24733" do
        d4 = Day4.new()
        expect(d4.part_1).to eq(24733)
      end
    end

    describe "part_2" do
      it "should come up with nil" do
        d4 = Day4.new()
        expect(d4.part_2).to eq(nil)
      end
    end
  end
end

// from https://www.reddit.com/r/adventofcode/comments/3w192e/day_9_solutions/cxso11a
export default function permute(input, pusher = (acc, arr) => acc.push(arr.slice()), accumulator = []) {
  const used = [];
  function genPermutations() {
    if (input.length === 0) {
      pusher(accumulator, used);
    }

    for (let i = 0; i < input.length; i++) {
      const [ch] = input.splice(i, 1);
      used.push(ch);
      genPermutations();
      input.splice(i, 0, ch);
      used.pop();
    }
  }

  genPermutations();
  return accumulator;
}

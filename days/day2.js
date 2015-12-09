import INPUT from '../inputs/input2';

let totalWrappingPaper = 0;
let totalRibbon = 0;

function calculateWrappingPaper(l, w, h) {
  const side1 = l * w;
  const side2 = w * h;
  const side3 = l * h;
  const minSide = Math.min(side1, side2, side3);

  return (2 * side1) + (2 * side2) + (2 * side3) + minSide;
}

function calculateRibbon(l, w, h) {
  const maxSide = Math.max(l, w, h);

  // calculate the wrong perimeter, then get rid of the max side's calculation
  const perimeter = (2 * l) + (2 * w) + (2 * h) - (2 * maxSide);
  const volume = l * w * h;

  return perimeter + volume;
}

for (const gift of INPUT) {
  const tokens = gift.split('x');
  const l = parseInt(tokens[0], 10);
  const w = parseInt(tokens[1], 10);
  const h = parseInt(tokens[2], 10);

  totalWrappingPaper += calculateWrappingPaper(l, w, h);
  totalRibbon += calculateRibbon(l, w, h);
}

console.log('Part 1 totalWrappingPaper: ' + totalWrappingPaper);
console.log('Part 1 totalRibbon: ' + totalRibbon);

import INPUT from '../inputs/input3';

const trackerPart1 = { '0,0': true, 'numUnique': 1 };
const trackerPart2 = { '0,0': true, 'numUnique': 1 };
const santaPart1 = { 'x': 0, 'y': 0 };
const santaPart2 = { 'x': 0, 'y': 0 };
const roboSantaPart2 = { 'x': 0, 'y': 0 };

function performMove(move, location, tracker) {
  switch (move) {
    case '^':
      location.y++;
      break;
    case 'v':
      location.y--;
      break;
    case '<':
      location.x--;
      break;
    case '>':
      location.x++;
      break;
    default:
      console.log('Unknown move: ' + move);
  }

  const coords = location.x + ',' + location.y;

  if (!tracker[coords]) {
    tracker[coords] = true;
    tracker.numUnique++;
  }
}

for (let i = 0; i < INPUT.length; i++) {
  const move = INPUT.charAt(i);
  performMove(move, santaPart1, trackerPart1);

  if (i % 2 === 0) {
    performMove(move, santaPart2, trackerPart2);
  } else {
    performMove(move, roboSantaPart2, trackerPart2);
  }
}

console.log('Part 1 unique houses: ' + trackerPart1.numUnique);
console.log('Part 2 unique houses: ' + trackerPart2.numUnique);

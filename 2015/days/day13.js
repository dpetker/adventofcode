import INPUT from '../inputs/input13';
import permute from '../utils/permutations';

// person name -> all other people -> happiness +/-
const map = {};
const names = [];

function parseInput() {
  INPUT.forEach(seating => {
    const tokens = seating.split(' ');
    if (!map[tokens[0]]) {
      map[tokens[0]] = {};
      names.push(tokens[0]);
    }

    let multiplier = 1;
    if (tokens[2] === 'lose') {
      multiplier = -1;
    }

    const units = parseInt(tokens[3], 10);
    const other = tokens[10].slice(0, -1);

    map[tokens[0]][other] = units * multiplier;
  });
}

function findHappiness(table) {
  let happiness = 0;

  table.forEach((person, index) => {
    if (person === 'me') {
      return;
    }

    const next = (index + 1) % table.length;
    const prev = (index - 1) > -1 ? index - 1 : table.length - 1;

    if (table[next] !== 'me') {
      happiness += map[person][table[next]];
    }

    if (table[prev] !== 'me') {
      happiness += map[person][table[prev]];
    }
  });

  return happiness;
}

parseInput();

let currMax = Number.MIN_VALUE;
for (const table of permute(names)) {
  const tableHappiness = findHappiness(table);
  currMax = (tableHappiness > currMax) ? tableHappiness : currMax;
}

console.log('Max happiness (Part 1): ' + currMax);

currMax = Number.MIN_VALUE;
names.push('me');
for (const table of permute(names)) {
  const tableHappiness = findHappiness(table);
  currMax = (tableHappiness > currMax) ? tableHappiness : currMax;
}

console.log('Max happiness (Part 2): ' + currMax);

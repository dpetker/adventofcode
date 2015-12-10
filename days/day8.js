import fs from 'fs';

const rawFile = fs.readFileSync('./inputs/input8.txt', 'utf8');
const INPUT = rawFile.trim().split('\n');

function findDiff(mapFn) {
  return INPUT.reduce((total, line) => {
    return total + mapFn(line);
  }, 0);
}

console.log('Part 1 diff: ' + findDiff(line => {
  return line.length - eval(line).length; // eslint-disable-line no-eval
}));

console.log('Part 2 diff: ' + findDiff(line => {
  return JSON.stringify(line).length - line.length;
}));

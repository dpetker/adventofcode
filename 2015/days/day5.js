import INPUT from '../inputs/input5';

const DISALLOWED_SUBSTRINGS = [
  'ab',
  'cd',
  'pq',
  'xy',
];

let niceStrPart1Count = 0;
let niceStrPart2Count = 0;

function checkVowels(test) {
  const matches = test.match(/[aeiou]/g);
  return matches && matches.length > 2;
}

function checkConsonantRun(test) {
  const matches = test.match(/([a-z])\1/g);
  return matches && matches.length > 0;
}

function checkInvalidSubstrings(test) {
  let hasInvalid = false;

  for (const substr of DISALLOWED_SUBSTRINGS) {
    if (test.includes(substr)) {
      hasInvalid = true;
      break;
    }
  }

  return !hasInvalid;
}

function checkPairs(test) {
  const matches = test.match(/([a-z][a-z])[a-z]*\1/g);
  return matches && matches.length > 0;
}

function checkRepeat(test) {
  const matches = test.match(/([a-z])[a-z]\1/g);
  return matches && matches.length > 0;
}

for (const test of INPUT) {
  const token = test.toLowerCase();
  if (checkVowels(token) && checkConsonantRun(token) && checkInvalidSubstrings(token)) {
    niceStrPart1Count++;
  }

  if (checkPairs(token) && checkRepeat(token)) {
    niceStrPart2Count++;
  }
}

console.log('Part 1 nice string count: ' + niceStrPart1Count);
console.log('Part 2 nice string count: ' + niceStrPart2Count);

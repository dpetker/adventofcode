let seed = '1113222113';

function generateLookAndSay(sequence) {
  return sequence.match(/(\d)\1*/g).map(s => s.length + s[0]).join('');
}

for (let i = 0; i < 40; i++) {
  seed = generateLookAndSay(seed);
}

console.log('Part 1: ' + seed.length);

for (let i = 0; i < 10; i++) {
  seed = generateLookAndSay(seed);
}

console.log('Part 1: ' + seed.length);

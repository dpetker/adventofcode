import INPUT from '../inputs/input9';

const uniqueLocations = [];
const routes = INPUT.reduce((currentRoutes, line) => {
  const [path, dist] = line.split(' = ');
  const [from, to] = path.split(' to ');
  currentRoutes[from] = currentRoutes[from] || {};
  currentRoutes[to] = currentRoutes[to] || {};

  currentRoutes[from][to] = parseInt(dist, 10);
  currentRoutes[to][from] = parseInt(dist, 10);

  if (!uniqueLocations.includes(from)) {
    uniqueLocations.push(from);
  }

  if (!uniqueLocations.includes(to)) {
    uniqueLocations.push(to);
  }

  return currentRoutes;
}, {});

// from https://www.reddit.com/r/adventofcode/comments/3w192e/day_9_solutions/cxso11a
function permute(input, pusher = (acc, arr) => acc.push(arr.slice()), accumulator = []) {
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

function findPathWeight(path) {
  let weight = 0;
  for (let i = 0; i < path.length - 1; i++) {
    const from = path[i];
    const to = path[i + 1];

    weight += routes[from][to];
  }

  return weight;
}

const permuatations = permute(uniqueLocations);

let currMin = Number.MAX_VALUE;
let currMax = Number.MIN_VALUE;
for (const path of permuatations) {
  const pathWeight = findPathWeight(path);

  currMin = (pathWeight < currMin) ? pathWeight : currMin;
  currMax = (pathWeight > currMax) ? pathWeight : currMax;
}

console.log('Min weight: ' + currMin);
console.log('Max weight: ' + currMax);

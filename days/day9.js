import INPUT from '../inputs/input9';
import permute from '../utils/permutations';

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

function findPathWeight(path) {
  let weight = 0;
  for (let i = 0; i < path.length - 1; i++) {
    const from = path[i];
    const to = path[i + 1];

    weight += routes[from][to];
  }

  return weight;
}

const permutations = permute(uniqueLocations);

let currMin = Number.MAX_VALUE;
let currMax = Number.MIN_VALUE;
for (const path of permutations) {
  const pathWeight = findPathWeight(path);

  currMin = (pathWeight < currMin) ? pathWeight : currMin;
  currMax = (pathWeight > currMax) ? pathWeight : currMax;
}

console.log('Min weight: ' + currMin);
console.log('Max weight: ' + currMax);

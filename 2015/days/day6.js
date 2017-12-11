import INPUT from '../inputs/input6';
import _ from 'lodash';

// Set up our grid
const grid = [];
for (let i = 0; i < 1000; i++) {
  grid.push([]);
  for (let j = 0; j < 1000; j++) {
    grid[i].push(0);
  }
}

function fillRange(startX, startY, endX, endY, mapFn) {
  for (let i = startX; i <= endX; i++) {
    for (let j = startY; j <= endY; j++) {
      grid[i][j] = mapFn(grid[i][j]);
    }
  }
}

function turnLightsOn(startX, startY, endX, endY) {
  fillRange(startX, startY, endX, endY, n => {
    return n + 1;
  });
}

function turnLightsOff(startX, startY, endX, endY) {
  fillRange(startX, startY, endX, endY, n => {
    return n === 0 ? 0 : n - 1;
  });
}

function toggleLights(startX, startY, endX, endY) {
  fillRange(startX, startY, endX, endY, n => {
    return n + 2;
  });
}

function convert(n) {
  return parseInt(n, 10);
}

function reduceGrid() {
  return _.reduce(grid, (total, arr) => {
    return total + _.reduce(arr, (runningTotal, item) => {
      return runningTotal + item;
    }, 0);
  }, 0);
}

for (const action of INPUT) {
  let tokens = action.split(' ');

  if (tokens[0] === 'turn') {
    tokens[1] = 'turn ' + tokens[1];
    tokens = _.slice(tokens, 1);
  }

  const startTokens = _.map(tokens[1].split(','), convert);
  const endTokens = _.map(tokens[3].split(','), convert);

  switch (tokens[0]) {
    case 'turn on':
      turnLightsOn(
        startTokens[0],
        startTokens[1],
        endTokens[0],
        endTokens[1]
      );
      break;
    case 'turn off':
      turnLightsOff(
        startTokens[0],
        startTokens[1],
        endTokens[0],
        endTokens[1]
      );
      break;
    case 'toggle':
      toggleLights(
        startTokens[0],
        startTokens[1],
        endTokens[0],
        endTokens[1]
      );
      break;
    default:
      console.log('Unknown action: ' + action);
  }
}

console.log('Lights: ' + reduceGrid());

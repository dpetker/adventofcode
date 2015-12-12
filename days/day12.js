import INPUT from '../inputs/input12';
import _ from 'lodash';

function reduceAll(total, elem) {
  switch (typeof elem) {
    case 'number':
      return total + elem;
    case 'object':
      return _.reduce(elem, reduceAll, total);
    case 'string':
      return total;
    default:
      console.log('Unknown typeof: ' + typeof elem);
      return total;
  }
}

function reducePart2(total, elem) {
  switch (typeof elem) {
    case 'number':
      return total + elem;
    case 'object':
      if (elem.constructor === Array || !_.includes(elem, 'red')) {
        return _.reduce(elem, reducePart2, total);
      }
      return total;
    case 'string':
      return total;
    default:
      console.log('Unknown typeof: ' + typeof elem);
      return total;
  }
}

console.log('Part 1: ' + _.reduce(INPUT, reduceAll, 0));
console.log('Part 2: ' + _.reduce(INPUT, reducePart2, 0));

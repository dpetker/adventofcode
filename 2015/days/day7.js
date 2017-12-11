import INPUT from '../inputs/input7';

const circuit = {};

class Wire {
  constructor(id, inputs) {
    this._id = id;
    this._inputs = inputs;
    this._resolvedValue = -1;
  }

  resolve() {
    // Comment out for part 1 solution
    if (this._id === 'b') {
      this._resolvedValue = 956;
      return this._resolvedValue;
    }

    if (this._resolvedValue !== -1) {
      return this._resolvedValue;
    }

    if (/^[0-9]+$/.test(this._inputs)) {
      this._resolvedValue = parseInt(this._inputs, 10);
      return this._resolvedValue;
    }

    const tokens = this._inputs.split(' ');

    if (tokens[0] === 'NOT') {
      this._resolvedValue = (~circuit[tokens[1]].resolve()) & 0xFFFF;
      return this._resolvedValue;
    }

    if (tokens.length === 1) {
      // direct pass from another Wire
      this._resolvedValue = circuit[tokens[0]].resolve();
      return this._resolvedValue;
    }

    try {
      const leftValue = /^[0-9]+$/.test(tokens[0]) ? parseInt(tokens[0], 10) : circuit[tokens[0]].resolve();
      const rightValue = /^[0-9]+$/.test(tokens[2]) ? parseInt(tokens[2], 10) : circuit[tokens[2]].resolve();

      switch (tokens[1]) {
        case 'AND':
          this._resolvedValue = (leftValue & rightValue) & 0xFFFF;
          break;
        case 'OR':
          this._resolvedValue = (leftValue | rightValue) & 0xFFFF;
          break;
        case 'LSHIFT':
          this._resolvedValue = (leftValue << rightValue) & 0xFFFF;
          break;
        case 'RSHIFT':
          this._resolvedValue = (leftValue >>> rightValue) & 0xFFFF;
          break;
        default:
          console.log('Unknown operator: ' + tokens[1]);
          this._resolvedValue = -1;
          break;
      }
      return this._resolvedValue;
    } catch (e) {
      console.log(this);
      console.log(e);
      throw e;
    }
  }
}

for (const bit of INPUT) {
  const tokens = bit.split('->');

  const id = tokens[1].trim();
  const input = tokens[0].trim();

  circuit[id] = new Wire(id, input);
}

console.log('Wire a signal: ' + circuit.a.resolve());

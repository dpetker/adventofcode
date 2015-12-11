let part1Input = 'vzbxkghb';

function generateNextPassword(current) {
  const charArray = current.split('');
  for (let i = charArray.length - 1; i >= 0; i--) {
    if (charArray[i] === 'z') {
      charArray[i] = 'a';
    } else {
      charArray[i] = String.fromCharCode(current.charCodeAt(i) + 1);
      break;
    }
  }

  return charArray.join('');
}

function testCharRun(pass) {
  return /(abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)/.test(pass);
}

function testInvalidChars(pass) {
  return !(/[i|o|l]/.test(pass));
}

function testPairs(pass) {
  return /([a-z])\1[a-z]*([a-z])\2/g.test(pass);
}

function testPassword(pass) {
  return testInvalidChars(pass) && testCharRun(pass) && testPairs(pass);
}

let currPwd = generateNextPassword(part1Input);
while (!testPassword(currPwd)) {
  currPwd = generateNextPassword(currPwd);
}

console.log('Part 1: ' + currPwd);

currPwd = generateNextPassword(currPwd);
while (!testPassword(currPwd)) {
  currPwd = generateNextPassword(currPwd);
}

console.log('Part 2: ' + currPwd);

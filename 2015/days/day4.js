import md5 from 'md5';

const SECRET = 'yzbqklnj';
let salt = 0;

while (true) { // eslint-disable-line no-constant-condition
  const key = md5(SECRET + salt);

  if (key.substr(0, 6) === '000000') {
    break;
  }

  salt++;
}

console.log('Salt: ' + salt);

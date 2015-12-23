import SPEEDS from '../inputs/input14';

const DURATION = 2503;
const reindeer = [];
const race = [];

class Reindeer {
  constructor(name, speed, runLen, restLen) {
    this._name = name;
    this._speed = speed;
    this._runLen = runLen;
    this._restLen = restLen;

    this._path = [];
    for (let i = 0; i < this._runLen; i++) {
      this._path.push(speed);
    }

    for (let i = 0; i < this._restLen; i++) {
      this._path.push(0);
    }

    this._totalRace = [];
  }

  runRace() {
    let distance = 0;

    for (let i = 0; i < DURATION; i++) {
      distance += this._path[i % this._path.length];
      this._totalRace.push(distance);
    }

    return { name: this._name, distance };
  }

  distanceAt(index) {
    return this._totalRace[index];
  }

  getName() {
    return this._name;
  }
}

function parseSpeeds() {
  SPEEDS.forEach(line => {
    const tokens = line.split(' ');
    const deer = new Reindeer(
      tokens[0],
      parseInt(tokens[3], 10),
      parseInt(tokens[6], 10),
      parseInt(tokens[13], 10)
    );

    reindeer.push(deer);
    race.push(deer.runRace());
  });
}

function findFurthest(currMax, deer) {
  if (deer.distance > currMax.distance) {
    return deer;
  }

  return currMax;
}

parseSpeeds();

const race1Deer = race.reduce(findFurthest, { name: 'me', distance: 0 });

console.log('Race 1:', race1Deer);

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

const race2Leaderboard = {
  'Dasher': 0,
  'Dancer': 0,
  'Prancer': 0,
  'Vixen': 0,
  'Comet': 0,
  'Cupid': 0,
  'Donner': 0,
  'Blitzen': 0,
  'Rudolph': 0,
};

function accumLeaderboard(leader, thisSec) {
  thisSec.forEach(deer => {
    if (deer.distance === leader.distance) {
      race2Leaderboard[deer.name]++;
    }
  });
}

for (let i = 0; i < DURATION; i++) {
  const thisSec = reindeer.map(deer => {
    return { name: deer.getName(), distance: deer.distanceAt(i) };
  });

  const thisLeader = thisSec.reduce(findFurthest, { distance: 0 });
  accumLeaderboard(thisLeader, thisSec);
}

console.log(race2Leaderboard);

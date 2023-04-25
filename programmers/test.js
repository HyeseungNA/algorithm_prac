const arr = [
  [1, 2, 3],
  [2, 4, 5],
  [1, 2, 3],
  [6, 7, 8],
  [1, 2, 3]
];

const map = new Map();
let count = 0;

for (let i = 0; i < arr.length; i++) {
  const key = arr[i].join('');
  if (map.has(key)) {
    map.set(key, map.get(key) + 1);
  } else {
    map.set(key, 1);
    console.log(key)
  }
}

for (const value of map.values()) {
  if (value >= 2) {
    count++;
  }
}





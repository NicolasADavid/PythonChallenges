function fibRecursive(n) {
  callCount++;
  if (n === 1 || n === 2) {
    return 1;
  }

  return fibRecursive(n - 1) + fibRecursive(n - 2);
}

let callCount = 0;
console.log(`fibRecursive(${10}) = ${fibRecursive(10)}, call count: ${callCount}`);

callCount = 0;
console.log(`fibRecursive(${12}) = ${fibRecursive(12)}, call count: ${callCount}`);
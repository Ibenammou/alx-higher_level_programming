#!/usr/bin/node

// define the factorial function
function factorial (n) {
  if (isNaN(n) || n < 0) {
    return (1);
  }

  if (n === 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

// Get the first arg from process.argv
const arg = parseInt(process.argv[2]);

// Use console.log(...) to print
console.log(factorial(arg));

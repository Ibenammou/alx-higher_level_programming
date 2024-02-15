#!/usr/bin/node

// Get the first arg from process.argv
const arg = process.argv[2];

// Convert the arg to an int
const num = parseInt(arg);

// Use console.log(...) to print
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}

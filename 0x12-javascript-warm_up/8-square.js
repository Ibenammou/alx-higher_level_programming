#!/usr/bin/node

// check the first argument from process.argv
const arg = process.argv[2];

// convert the arg to an int
const size = parseInt(arg);

// check if the arg is a valid positive int
if (isNaN(size)) {
  console.log('Missing size');
} else if (size <= 0) {
  // use a loop to print a square of size x size
  process.exit();
}
for (let x = 0; x < size; x++) {
  console.log('X'.repeat(size));
}

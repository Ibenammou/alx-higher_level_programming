#!/usr/bin/node

// Check the number of command-line arguments
const numArgs = process.argv.length;

// Use console.log(...) to print
if (numArgs === 2) {
  console.log('No argument');
} else if (numArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}


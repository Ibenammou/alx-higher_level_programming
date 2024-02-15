#!/usr/bin/node

// Get the first argument from process.argv
const firstArg = process.argv[2];

// Use console.log(...) to print
if (typeof firstArg === 'undefined') {
  console.log('No argument');
} else {
  console.log(firstArg);
}

#!/usr/bin/node

// define the add function
function add (a, b) {
  return a + b;
}

// Get the first and second args from process.argv
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

// Use console.log(...) to print the addition
console.log(add(arg1, arg2));

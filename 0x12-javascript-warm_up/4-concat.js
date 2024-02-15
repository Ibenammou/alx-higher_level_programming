#!/usr/bin/node

// Get the first and second args from process.argv
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Use console.log(...) to print
console.log(`${arg1 || 'undefined'} is ${arg2 || 'undefined'}`);

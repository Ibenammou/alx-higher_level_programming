#!/usr/bin/node

// Get the args from process.argv starting from 3rd element
const args = process.argv.slice(2);

// convert the args to an array of int
const integers = args.map(arg => parseInt(arg));

// sort the array in descending order
const sortedIntegers = integers.sort((a, b) => b - a);

// Print the second biggest integer or 0 if not available
console.log(sortedIntegers[1] || 0);

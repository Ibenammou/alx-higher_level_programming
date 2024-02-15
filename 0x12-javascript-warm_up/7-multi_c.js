#!/usr/bin/node

// Get the first arg from process.argv
const arg = process.argv[2];

// convert the arg to an int
const num = parseInt(arg);

// check if the arg is a valid positve int
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  // Use a loop to print x times
  for (let x = 0; x < num; x++) {
    console.log('C is fun');
  }
}

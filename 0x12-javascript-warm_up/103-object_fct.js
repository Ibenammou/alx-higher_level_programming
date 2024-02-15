#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

// define the incr function
myObject.incr = function () {
  this.value++;
};

// assign the anonymous function to the incr property
// myObject.incr = incr;

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

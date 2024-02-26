#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let x = 0; x < this.height; x++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;

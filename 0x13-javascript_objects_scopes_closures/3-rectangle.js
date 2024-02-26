#!/usr/bin/node

class Rectangle {
  print () {
    for (let x = 0; x < this.height; x++) {
      let rw = '';
      for (let y = 0; y < this.width; y++) {
        rw += 'X';
      }
      console.log(rw);
    }
  }

  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return 'Rectangle {}';
    }
    this.width = w;
    this.height = h;
  }
  /*
  print() {
    for (let x = 0; x < this.height; x++) {
      let rw = '';
      for (let y = 0; y < this.width; y++) {
        rw += 'X';
      }
      console.log(rw);
    }
  }
  */
}

module.exports = Rectangle;

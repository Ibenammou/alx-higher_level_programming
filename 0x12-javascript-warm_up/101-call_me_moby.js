#!/usr/bin/node

// define the callMeMoby function
function callMeMoby (x, theFunction) {
  for (let y = 0; y < x; y++) {
    theFunction();
  }
}

// Export the callMeMoby function
module.exports = { callMeMoby };

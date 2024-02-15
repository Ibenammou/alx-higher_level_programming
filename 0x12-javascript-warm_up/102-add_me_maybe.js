#!/usr/bin/node

// define the addMeMaybe function
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

// export the function
module.exports = { addMeMaybe };

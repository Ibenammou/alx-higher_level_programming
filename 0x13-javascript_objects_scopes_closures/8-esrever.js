#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  for (let x = list.length - 1; x >= 0; x--) {
    reversedList.push(list[x]);
  }
  return reversedList;
};

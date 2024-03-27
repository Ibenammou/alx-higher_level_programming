#!/usr/bin/node

// Script tp get the contents of a webpage and stores in a file

const request = require('request');
const fs = require('fs');

request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));

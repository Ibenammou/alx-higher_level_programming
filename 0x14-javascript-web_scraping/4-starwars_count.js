#!/usr/bin/node

// Script that uses the request module to make a GET request
// to the Star Wars API endpoint and then filter the films
// where the character "Wedge Antilles"

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let num = 0;

    for (const filmIndex in films) {
      const filmChars = films[filmIndex].characters;

      for (const charIndex in filmChars) {
        if (filmChars[charIndex].includes('18')) {
          num++;
        }
      }
    }

    console.log(num);
  } else {
    console.log('An error occurred. Status code: ' + response.statusCode);
  }
});

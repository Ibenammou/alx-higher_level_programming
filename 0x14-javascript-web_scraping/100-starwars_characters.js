#!/usr/bin/node

// Script to print all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Funciton to get character details
    const getCharacterDetails = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
          } else {
            const characterData = JSON.parse(charBody);
            resolve(characterData.name);
          }
        });
      });
    };

    // Use Promise.all to handle asynchronous requests
    Promise.all(characters.map(getCharacterDetails))
      .then(characterNames => {
        // Display one character name per line
        characterNames.forEach(name => console.log(name));
      })
      .catch(err => console.error(err));
  }
});

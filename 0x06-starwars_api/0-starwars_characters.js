#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as a command line argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    if (characters.length === 0) {
      console.log('No characters found for this movie.');
    } else {
      console.log(`Characters in ${film.title}:`);
      characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error('Error fetching character:', charError);
          } else if (charResponse.statusCode !== 200) {
            console.error('Unexpected status code for character:', charResponse.statusCode);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
          }
        });
      });
    }
  }
});

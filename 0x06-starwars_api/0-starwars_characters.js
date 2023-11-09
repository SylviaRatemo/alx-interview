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
      const sortedCharacters = [];

      // Use a recursive function to handle asynchronous character requests
      function getCharacter(index) {
        if (index === characters.length) {
          // All characters fetched, now sort and print
          sortedCharacters.sort();
          sortedCharacters.forEach((characterName) => {
            console.log(characterName);
          });
        } else {
          // Fetch character and add to sorted list
          const characterUrl = characters[index];
          request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
              console.error('Error fetching character:', charError);
            } else if (charResponse.statusCode !== 200) {
              console.error('Unexpected status code for character:', charResponse.statusCode);
            } else {
              const character = JSON.parse(charBody);
              sortedCharacters.push(character.name);
              // Continue to the next character
              getCharacter(index + 1);
            }
          });
        }
      }

      // Start fetching characters
      getCharacter(0);
    }
  }
});

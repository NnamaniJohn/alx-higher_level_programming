#!/usr/bin/node
// a script that reads and prints the content of a file.


const file = process.argv[1];
const fileStream = require('fs');
fileStream.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});

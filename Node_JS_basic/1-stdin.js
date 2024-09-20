const readline = require('readline');
const lineReader = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
lineReader.question('Welcome to Holberton School, what is your name?\n', (username) => {
  console.log('Your name is: ' + username);
});

lineReader.on('close', () => {
  console.log('This important software is now closing');
});

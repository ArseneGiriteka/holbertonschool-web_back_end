const readline = require('readline');

console.log("Welcome to Holberton School, what is your name?");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('', (userInput) => {
  const username = userInput.toString().trim();
  console.log('Your name is: ' + username);
  rl.close();
});

process.stdin.on('end', () => {
  console.log("This important software is now closing");
});

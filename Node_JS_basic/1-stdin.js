const process = require('process');
process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const my_name = process.stdin.read();
  if (my_name) {
    process.stdout.write(`Your name is: ${my_name}`);
  }
});
process.stdin.on('end', () => {
  console.log('This important software is now closing');
});

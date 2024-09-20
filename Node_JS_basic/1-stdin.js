var process = require('process');

process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  var my_name = process.stdin.read();
  if (my_name) {
    process.stdout.write(`Your name is: ${my_name}`);
  }
});
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (data) => {
  const inputName = data.toString().trim();

  console.log(`Your name is: ${inputName}`);
  if (process.stdin.isTTY) {
    process.exit();
  }
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});

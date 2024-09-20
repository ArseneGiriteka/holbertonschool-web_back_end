const http = require('http');

const app = http.createServer((request, result) => {
  result.write('Hello Holberton School!');
  result.end();
});

app.listen((1245), 'localhost', () => {});
